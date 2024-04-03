#!/usr/bin/env python3
"""hypermedia pagination module"""
import math
from typing import List, Tuple, Dict

index_range = __import__('0-simple_helper_function').index_range

def get_hyper(self, page:int = 1, page_size: int = 10):
    """returns a dictionary of hypermedia key-value pairs"""
    start_index, end_index = index_range(page, page_size)
    prev_page= None
    if (page > 1):
        prev_page = page - 1

    next_page = None
    if (len(self.dataset()) > end_index):
        next_page = page + 1

    total_pages = int(len(self.dataset()) / 10)
    if (page_size > 0):
        total_pages = int(len(self.dataset()) / page_size)

    hyper_dict = {
        "page_size": len(self.get_page(page, page_size)),
        "page": page,
        "data": self.get_page(page, page_size),
        "next_page": next_page,
        "prev_page": prev_page,
        "total_pages": total_pages
    }
    return hyper_dict