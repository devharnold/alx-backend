#!/usr/bin/env python3
"""Hyperdmedia pagination module
"""
from typing import List
index_range = __import__('0-simple_helper_function').index_range


def get_hyper_index(self, index: int = None, page: int = 1, page_size: int = 20):
    """return dictionary of the hypermedia key-value pairs"""
    assert type(index) == int
    assert type(page_size) == int
    assert index >= 0
    assert index < len(self.indexed_dataset())
    csv = self.indexed_dataset()
    data = []
    next_index = index
    for item in range(page_size):
        while not csv.get(next_index):
            next_index += 1
        data.append(csv.get(next_index))
        next_index += 1
    return {
        "index": index,
        "data": data,
        "page_size": page_size,
        "next_index": next_index
        }