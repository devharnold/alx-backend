#!/usr/bin/env python3
"""fifo cache module"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """class caching system"""
    def __init__(self, capacity):
        """Initialize class fifocache"""
        super().__init__()
        self.capacity = capacity
        self.cache = OrderedDict()
        

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
        if len(self.cache) >= self.capacity:
            if key not in self.cache:
                discard = next(iter(self.cache))
                del self.cache[discard]

        self.cache[key] = item

    def get(self, key):
        """
        must return the value in `self.cache_data` linked to key
        return None if key is none
        """
        if key in self.cache:
            return self.cache[key]
        return None