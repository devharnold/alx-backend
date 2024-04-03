#!/usr/bin/env python3
"""fifo cache module"""
import sys
import os

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """class caching system"""
    def __init__(self):
        """Initialize class fifocache"""
        self.cache_data = {}

    def 