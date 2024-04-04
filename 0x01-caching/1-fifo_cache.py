#!/usr/bin/env python3
"""First-In-First-Out caching module"""
from collections import OrderedDict
from base_caching import BaseCaching
class FIFOCache(BaseCaching):
    """class caching system"""
    def __init__(self):
        """Initialize class fifocache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        must assign to the dictionary `self.cache_data` the item value for the key `key`
        if `key` or `item` is None -> do nothing
        if number of items in self.cache_data > `BaseCaching.MAX_ITEMS`:
            ->must discard the first item put in cache(FIFO algorithm)
            ->must print `DISCARD` with the key dicarded
        Attributes:
            item: element
            key: caching steps
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        must return the value in `self.cache_data` linked to key
        return None if key is none
        """
        return self.cache_data.get(key, None)