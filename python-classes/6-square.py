#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError ('size must be an integer')
        elif size < 0:
            raise ValueError ('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise  TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2
    
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
