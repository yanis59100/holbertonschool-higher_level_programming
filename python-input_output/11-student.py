#!/usr/bin/python3
"""defines function write class of student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialisation of attribute student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)