#!/usr/bin/python3
def add_integer(a, b=98):
    """ Add new integer or floats a and b value 98

    If a and b are not integers or floats
    

    Return integer a + interger b
    """    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
