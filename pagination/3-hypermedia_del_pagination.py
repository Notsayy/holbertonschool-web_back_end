#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.

This module provides a Server class that enables paginated access to a dataset
of popular baby names, with resilience to deletions in the underlying data.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.

    This class provides methods to load the dataset, index it by position,
    and retrieve paginated data starting from a specified index. It is
    designed to be resilient to deletions: if a record at a given index
    is missing, it skips to the next available record.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the Server instance with dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of rows, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Creates and caches an indexed version of the dataset.

        Returns:
            Dict[int, List]: A dictionary mapping index positions to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of data starting from a given index, skipping any deleted entries.

        Args:
            index (int, optional): The starting index for pagination. Defaults to 0 if None.
            page_size (int, optional): The number of items to return in the page. Defaults to 10.

        Returns:
            Dict: A dictionary containing:
                - index (int): The original start index,
                - next_index (int): The index to use for the next page,
                - page_size (int): The actual number of items returned,
                - data (List): The page of data.
        """
        indexed_data = self.indexed_dataset()
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert index < len(self.dataset())
        data = []
        current_index = index
        for _ in range(page_size):
            while current_index not in indexed_data and current_index < len(
                self.dataset()
            ):
                current_index += 1
            if current_index >= len(self.dataset()):
                break

            data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
