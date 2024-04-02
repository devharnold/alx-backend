#!/usr/bin/env python3
'''simple pagination'''
import csv
import math
from typing import List, Tuple

from simple_helper_function import index_range

def get_page(page=1, page_size=10) -> int:
    '''return a page of the dataset
    Attributes:
        assert - verify both arguments are integers greater than 0
        `index_range` - helper function to find the correct indexes to paginate the dataset and return
        the appropriate page of the dataset
    Return - if the input arguments are out of range (empty list)
    '''
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0
    with open('0x00-pagination/data.csv', 'r') as f:
        reader = csv.reader(f)
        dataset = [row for row in reader]
        start, end = index_range(page, page_size)
        return dataset[start:end]
    
    
