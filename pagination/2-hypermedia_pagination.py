#!/usr/bin/env python3

"""
This module provides a Server class for paginating a CSV dataset
of popular baby names, along with utility functions for pagination.
"""

import csv
import math
from typing import List, Dict, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a page of data.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: (start_index, end_index) representing the
        range of items to return for the given page.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): Path to the CSV data file.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance and dataset cache.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of rows (excluding the header).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset.

        Args:
            page (int): The current page number (1-indexed, must be > 0).
            page_size (int): The number of items per page (must be > 0).

        Returns:
            List[List]: The list of rows for the requested page.
                        Returns an empty list if the start index is out
                        of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end] if start < len(data) else []

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Optional[object]]:
        """
        Retrieve a page of the dataset with hypermedia pagination metadata.

        Args:
            page (int): The current page number (1-indexed, must be > 0).
            page_size (int): The number of items per page (must be > 0).

        Returns:
            Dict[str, Optional[object]]: A dictionary containing:
                - page_size (int): The actual number of items returned.
                - page (int): The current page number.
                - data (List[List]): The list of rows for the current page.
                - next_page (Optional[int]): The next page number, or None.
                - prev_page (Optional[int]): The previous page number, or None.
                - total_pages (int): The total number of available pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
