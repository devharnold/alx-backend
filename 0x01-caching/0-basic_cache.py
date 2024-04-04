#!/usr/bin/env python3
"""basic cache module"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):

    def put(self, key, item):
        """Must assign the dictionary
            self.cache_data -> the item value for the key
        Method should not do anything
        """
        if key and item:
            self.cache_data[key] = item
        else:
            return None
            
    def get(self, key):
        """
        Must return the value in `self.cache_data` linked to key
        Return None: if key -> None or not existing in self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
