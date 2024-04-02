#!/usr/bin/env python3
'''simple helper function'''
from typing import Tuple

def index_range(page, page_size) -> tuple:
    '''returns a tuple of size two containing a start index and an end index'''
    return ((page - 1) * page_size, page * page_size)