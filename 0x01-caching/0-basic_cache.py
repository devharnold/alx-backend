#!/usr/bin/env python3
"""basic cache module"""


BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
    class caching system
    """
    def __init__(self):
        """
        Initialize
        """
        self.cache_data = {}

    def put(self, key, item):
        """Must assign the dictionary
            self.cache_data -> the item value for the key
        Method should not do anything
        """
        for key, items in sorted(self.cache_data.keys()):
            if (key, items) is None:
                raise NotImplementedError("Cannot work with empty keys and items")
            
    def get(self, key):
        """
        Must return the value in `self.cache_data` linked to key
        Return None: if key -> None or not existing in self.cache_data
        """
        for key, items in sorted(self.cache_data.keys()):
            if (key) != self.cache_data():
                return None
            if (key) is None:
                return None