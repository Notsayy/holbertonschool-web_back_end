#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Deletion-resilient hypermedia pagination.
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys())
        assert index <= max_index

        data = []
        current = index
        collected = 0

        # Collect page_size items, skipping deleted indices
        while collected < page_size and current <= max_index:
            item = indexed_data.get(current)
            if item is not None:
                data.append(item)
                collected += 1
            current += 1

        next_index = current

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
