#!/usr/bin/env python3
"""This module defines a CountedIterator class that extends a basic iterator."""

class CountedIterator:
    """An iterator that counts the number of items iterated over."""
    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Raises StopIteration when no more items are available."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the number of items that have been iterated over."""
        return self.count
