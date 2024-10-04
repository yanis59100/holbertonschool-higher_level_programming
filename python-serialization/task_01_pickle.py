#!/usr/bin/python3
'''This module provides a function that pickles instances of data to a file.'''
import pickle


class CustomObject():
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''Pickles the object in a file.'''
        try:
            with open(filename, 'wb', ) as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''Returns an object from a pkl file.'''
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
