#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        print(''.join(str(s) for s in new_list))
        count = 0
        for elem in new_list:
            count += 1
        return count
    except IndexError:
        num = my_list[-1:]
        counter = 0
        for elem in my_list:
            counter += 1
        return 
