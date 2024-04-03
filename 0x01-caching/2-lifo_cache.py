#!/usr/bin/env python3
"""lifo cache module"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """class LIFOCache"""
    def __init__(self, capacity):
        """initialize"""
        super().__init__()
        self.capacity = capacity
        self.cache = OrderedDict

        self.cache_data = {}

    def put(self, key, item) -> dict:
        """
        must assign to the dictionary `self.cache_data` the item value for the key `key`
        if `key` or `item` is None -> do nothing
        if number of items in self.cache_data > `BaseCaching.MAX_ITEMS`:
            ->must discard the last item put in cache(LIFO algorithm)
            ->must print `DISCARD` with the key dicarded
        Attributes:
            item: element
            key: caching steps
        """
        if len(self.cache) >= self.capacity:
            if(key, item)not in self.cache:
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