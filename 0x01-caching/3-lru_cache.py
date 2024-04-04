#!/usr/bin/env python3
"""Least Recently Used Caching module.
"""

from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """Repr object allows store and retrieving items 
    with LRU algorithm when limit is reached"""
    def __init__(self):
        """Initializes cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item using key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)