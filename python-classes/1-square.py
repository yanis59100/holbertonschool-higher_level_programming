#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
