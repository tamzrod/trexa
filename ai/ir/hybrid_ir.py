"""
Hybrid IR (Information Retrieval) Module

Retrieves, ranks, compresses, and injects relevant context.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Callable, Protocol
from enum import Enum
import time


class RetrievalStrategy(Enum):
    """Strategy for retrieving context."""
    SEMANTIC = "semantic"  # Embedding-based similarity
    KEYWORD = "keyword"     # BM25 or similar
    HYBRID = "hybrid"      # Combination of both
    EXACT = "exact"        # Exact match


@dataclass
class RetrievedContext:
    """A piece of retrieved context."""
    content: str
    source: str
    relevance_score: float
    chunk_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass 
class CompressedContext:
    """Context after compression."""
    content: str
    compression_ratio: float
    token_count: int
    citations: List[str] = field(default_factory=list)


@dataclass
class IRConfig:
    """Configuration for the IR system."""
    max_retrieved: int = 10
    min_relevance_score: float = 0.5
    max_context_tokens: int = 32000
    compression_enabled: bool = True
    compression_ratio: float = 0.3
    retrieval_strategy: RetrievalStrategy = RetrievalStrategy.HYBRID
    
    # Ranking weights
    semantic_weight: float = 0.6
    keyword_weight: float = 0.4


class ContextRetriever(Protocol):
    """Protocol for context retrieval backends."""
    
    def retrieve(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[RetrievedContext]:
        """Retrieve relevant context for a query."""
        ...


class SimpleRetriever:
    """Simple keyword-based retriever (placeholder implementation)."""
    
    def __init__(self, documents: List[Dict[str, str]]):
        """
        Initialize with documents.
        
        Args:
            documents: List of documents with 'id', 'content', 'source' keys
        """
        self.documents = documents
    
    def retrieve(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[RetrievedContext]:
        """Simple keyword matching retrieval."""
        query_terms = set(query.lower().split())
        results = []
        
        for doc in self.documents:
            content_lower = doc['content'].lower()
            content_terms = set(content_lower.split())
            
            # Simple Jaccard similarity
            intersection = query_terms & content_terms
            union = query_terms | content_terms
            if union:
                score = len(intersection) / len(union)
            else:
                score = 0.0
            
            if score > 0.1:  # Minimum threshold
                results.append(RetrievedContext(
                    content=doc['content'],
                    source=doc.get('source', 'unknown'),
                    relevance_score=score,
                    chunk_id=doc.get('id'),
                    metadata=doc.get('metadata', {})
                ))
        
        # Sort by score and limit
        results.sort(key=lambda x: x.relevance_score, reverse=True)
        return results[:max_results]


class ContextRanker:
    """Ranks and filters retrieved context."""
    
    def __init__(self, config: IRConfig):
        self.config = config
    
    def rank(self, contexts: List[RetrievedContext]) -> List[RetrievedContext]:
        """Rank and filter contexts."""
        if not contexts:
            return []
        
        # Filter by minimum relevance
        filtered = [
            c for c in contexts
            if c.relevance_score >= self.config.min_relevance_score
        ]
        
        # Sort by relevance score
        filtered.sort(key=lambda x: x.relevance_score, reverse=True)
        
        # Limit to max results
        return filtered[:self.config.max_retrieved]
    
    def deduplicate(self, contexts: List[RetrievedContext]) -> List[RetrievedContext]:
        """Remove duplicate or near-duplicate contexts."""
        if not contexts:
            return []
        
        seen_content = set()
        unique = []
        
        for ctx in contexts:
            # Simple deduplication by first 100 chars
            content_hash = ctx.content[:100].lower().strip()
            if content_hash not in seen_content:
                seen_content.add(content_hash)
                unique.append(ctx)
        
        return unique


class ContextCompressor:
    """Compresses context to fit within token limits."""
    
    def __init__(self, config: IRConfig):
        self.config = config
    
    def compress(
        self,
        contexts: List[RetrievedContext],
        max_tokens: Optional[int] = None
    ) -> CompressedContext:
        """
        Compress multiple contexts into a single context.
        
        Args:
            contexts: List of retrieved contexts
            max_tokens: Maximum tokens allowed (uses config default if not provided)
            
        Returns:
            CompressedContext with merged content
        """
        if not contexts:
            return CompressedContext(
                content="",
                compression_ratio=1.0,
                token_count=0,
                citations=[]
            )
        
        max_tokens = max_tokens or self.config.max_context_tokens
        
        # Sort by relevance
        sorted_contexts = sorted(
            contexts,
            key=lambda x: x.relevance_score,
            reverse=True
        )
        
        # Build content with citations
        parts = []
        citations = []
        current_tokens = 0
        
        for i, ctx in enumerate(sorted_contexts, 1):
            # Estimate tokens (rough: 4 chars per token)
            est_tokens = len(ctx.content) // 4
            
            if current_tokens + est_tokens > max_tokens:
                # Try compression on remaining
                remaining = max_tokens - current_tokens
                if remaining < 100:
                    break
                # Add truncated content
                truncated = ctx.content[:remaining * 4]
                parts.append(f"[{i}] {truncated}...")
            else:
                parts.append(f"[{i}] {ctx.content}")
            
            current_tokens += est_tokens
            citations.append(f"[{i}] {ctx.source}")
        
        combined_content = "\n\n".join(parts)
        original_tokens = sum(len(c.content) // 4 for c in contexts)
        
        return CompressedContext(
            content=combined_content,
            compression_ratio=current_tokens / max(original_tokens, 1),
            token_count=current_tokens // 4,
            citations=citations
        )


class HybridIRSystem:
    """
    Hybrid Information Retrieval system.
    
    Pipeline:
    1. Retrieve context from sources
    2. Rank by relevance
    3. Compress to fit context limits
    4. Inject into prompt
    """
    
    def __init__(
        self,
        config: Optional[IRConfig] = None,
        retriever: Optional[ContextRetriever] = None
    ):
        self.config = config or IRConfig()
        self.retriever = retriever
        self.ranker = ContextRanker(self.config)
        self.compressor = ContextCompressor(self.config)
    
    def retrieve(
        self,
        query: str,
        max_results: Optional[int] = None
    ) -> List[RetrievedContext]:
        """
        Retrieve relevant context for a query.
        
        Args:
            query: The search query
            max_results: Override max results from config
            
        Returns:
            List of retrieved contexts
        """
        if not self.retriever:
            return []
        
        max_r = max_results or self.config.max_retrieved
        raw_results = self.retriever.retrieve(query, max_r)
        
        # Rank and deduplicate
        ranked = self.ranker.rank(raw_results)
        return self.ranker.deduplicate(ranked)
    
    def process(
        self,
        query: str,
        user_prompt: str,
        max_context_tokens: Optional[int] = None
    ) -> str:
        """
        Full IR pipeline: retrieve, compress, and inject context.
        
        Args:
            query: Search query for retrieval
            user_prompt: Original user prompt
            max_context_tokens: Override max context tokens
            
        Returns:
            Prompt with injected context
        """
        start_time = time.time()
        
        # Step 1: Retrieve
        contexts = self.retrieve(query)
        
        # Step 2: Compress
        compressed = self.compressor.compress(contexts, max_context_tokens)
        
        # Step 3: Inject
        elapsed_ms = (time.time() - start_time) * 1000
        
        if compressed.content:
            injected = (
                f"<CONTEXT>\n"
                f"Retrieved {len(contexts)} relevant documents "
                f"({elapsed_ms:.0f}ms retrieval time)\n\n"
                f"{compressed.content}\n\n"
                f"</CONTEXT>\n\n"
                f"<USER_PROMPT>\n{user_prompt}\n</USER_PROMPT>"
            )
        else:
            injected = user_prompt
        
        return injected
    
    def get_retrieval_stats(self) -> Dict[str, Any]:
        """Get retrieval system statistics."""
        return {
            "retrieval_strategy": self.config.retrieval_strategy.value,
            "max_retrieved": self.config.max_retrieved,
            "min_relevance_score": self.config.min_relevance_score,
            "compression_enabled": self.config.compression_enabled
        }


def create_ir_system(
    documents: Optional[List[Dict[str, str]]] = None,
    **config_kwargs
) -> HybridIRSystem:
    """
    Factory function to create an IR system.
    
    Args:
        documents: Initial documents to index
        **config_kwargs: Override config values
        
    Returns:
        Configured HybridIRSystem
    """
    config = IRConfig(**config_kwargs)
    
    if documents:
        retriever = SimpleRetriever(documents)
    else:
        retriever = None
    
    return HybridIRSystem(config=config, retriever=retriever)
