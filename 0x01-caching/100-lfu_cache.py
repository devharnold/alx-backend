#!/usr/bin/env python3
"""LFU Cache module.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """sort and retrieve items from a dictionary
    using the LRU algorithm when limit is reached.
    """
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds item in the cache."""
        if key is None or item is None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lru_key, _ = self.cache_data.popitem(False)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item


    def get(self, key):
        """return the values of cache data linked to key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)