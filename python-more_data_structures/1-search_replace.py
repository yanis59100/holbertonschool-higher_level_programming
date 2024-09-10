#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for  i in my_list:
        if i == 2:
            my_list[my_list.index(i)] = 89
    return my_list
