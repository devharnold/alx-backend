#!/usr/bin/env python3
'''simple pagination'''
import csv
import math
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range

def get_page(self, page:int = 1, page_size: int = 10) -> List[List]:
    '''return a page of the dataset
    Attributes:
        assert - verify both arguments are integers greater than 0
        `index_range` - helper function to find the correct indexes to paginate the dataset and return
        the appropriate page of the dataset
    Return - if the input arguments are out of range (empty list)
    '''
    assert type(page) == int
    assert type(page_size) == int
    assert page > 0
    assert page_size > 0

    start_index, end_index = index_range(page, page_size)
    if ((len(self.dataset()) < start_index) or (len(self.dataset()) < end_index)):
        return []
    
    paginated_names = []
    for i in range(start_index, end_index):
        paginated_names.append(self.dataset()[i])
    return paginated_names
    
    
