#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """
    Represent a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Return the width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Return the height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of the Rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Return the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Return the rectangle in string using #
        """
        if not (self.__height or self.__width):
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str.rstrip()

    def __repr__(self):
        """
        Return the string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message for every instance of Rectangle deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
