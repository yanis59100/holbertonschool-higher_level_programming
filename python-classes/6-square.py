#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.
            position (int, int): the position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Returns the size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the square.
        """
        return (self.position)

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value

    def area(self):
        """ Return the area of the Square """
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints in stdout the Square with the character # """
        if self.__size == 0:
            print()
            return

        [print("") for i in range (0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
