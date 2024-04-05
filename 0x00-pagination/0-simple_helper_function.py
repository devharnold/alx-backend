#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple

def index_range(page, page_size) -> tuple:
    """returns a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)