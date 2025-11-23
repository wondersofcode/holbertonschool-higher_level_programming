#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_list = []
    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
            sum += i
    return sum
