#!/usr/bin/python3
'''This module provides a function that writes JSON to a file.'''
import json


def serialize_and_save_to_file(data, filename):
    '''Writes a JSON representation of an object in a file.'''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    '''Returns an object from a JSON file.'''
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
