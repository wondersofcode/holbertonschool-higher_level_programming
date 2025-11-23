#!/usr/bin/python3
def no_c(my_string):
    ml = list(my_string)
    for i in range(len(ml)):
        if ml[i] == "c" or ml[i] == "C":
            ml[i] = ""
    return "".join(ml)
