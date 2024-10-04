#!/usr/bin/python3
'''This module provides utility to convert CSV to JSON'''
import csv
import json


def convert_csv_to_json(csv_filename):
    '''Writes data in contained in a CSV to a JSON file.'''
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(rows, json_file)
            return True
    except FileNotFoundError:
        return False
