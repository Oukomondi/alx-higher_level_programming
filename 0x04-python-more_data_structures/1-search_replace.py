#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    temp = []
    index = 0
    for items in new_list:
        if items == search:
            new_list[index] = replace
        index += 1

    return 
