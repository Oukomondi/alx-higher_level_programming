#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for item in my_list:
            if isinstance(item, (str, list)):
                my_list.remove(item)
        new_list = my_list[:x]
        count = 0
        for item in new_list:
            print("{:d}".format(item), end='')
            count += 1
        print("")
        return count
    except IndexError:
        for item in my_list:
            print("{:d}".format(item), end='')
