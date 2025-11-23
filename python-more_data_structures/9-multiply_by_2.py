#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_copy = a_dictionary.copy()
    for i in a_copy:
        a_copy[i] *= 2
    return a_copy
