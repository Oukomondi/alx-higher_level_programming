#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list(print(f"{key}: {a_dictionary[key]}") for key in sorted(a_dictionary))
