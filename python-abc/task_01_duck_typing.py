#!/usr/bin/env python3
"""Module for demonstrating shapes and their properties."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class for a circle."""
    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """Concrete class for a rectangle."""
    def __init__(self, width, height):
        """Initialize a rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a given shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
