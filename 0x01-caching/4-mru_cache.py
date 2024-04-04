#!/usr/bin/env python3
"""Most Recently Used caching module
"""
from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """Storing and retrieve items from a dictionary
    with an MRU algorithm when limit is reached.
    """
    def __init__(self):
        """Initializes cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cachee_data[key] = item

    def get(self, key):
        """Retrieve item using key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_ata.get(key, None)
