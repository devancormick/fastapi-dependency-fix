"""
Algolia search service integration.
"""

from typing import Optional, Dict, Any
import os


class AlgoliaService:
    """Service for interacting with Algolia search."""
    
    def __init__(self, app_id: Optional[str] = None, api_key: Optional[str] = None):
        """
        Initialize Algolia service.
        
        Args:
            app_id: Algolia application ID
            api_key: Algolia API key
        """
        self.app_id = app_id or os.getenv("ALGOLIA_APP_ID")
        self.api_key = api_key or os.getenv("ALGOLIA_API_KEY")
        self._client = None
        
        if self.app_id and self.api_key:
            try:
                from algoliasearch.search_client import SearchClient
                self._client = SearchClient.create(self.app_id, self.api_key)
            except ImportError as e:
                raise ImportError(
                    "Algolia SDK not installed. Install with: pip install algoliasearch"
                ) from e
    
    def search(self, index_name: str, query: str, **kwargs) -> Dict[str, Any]:
        """
        Perform a search query.
        
        Args:
            index_name: Name of the Algolia index
            query: Search query string
            **kwargs: Additional search parameters
            
        Returns:
            Search results dictionary
        """
        if not self._client:
            raise RuntimeError("Algolia client not initialized")
        
        index = self._client.init_index(index_name)
        return index.search(query, **kwargs)
    
    def is_configured(self) -> bool:
        """Check if Algolia is properly configured."""
        return self._client is not None
