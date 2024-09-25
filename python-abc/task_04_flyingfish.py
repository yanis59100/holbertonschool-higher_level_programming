#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance in Python using a FlyingFish class"""


class Fish:
    """Represents a Fish with swimming behavior and a water habitat."""

    def swim(self):
        """Prints a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Represents a Bird with flying behavior and a sky habitat."""

    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """Prints a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message about the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")