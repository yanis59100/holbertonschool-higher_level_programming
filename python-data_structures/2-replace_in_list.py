#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list[3] = 9
    for i in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            return my_list
