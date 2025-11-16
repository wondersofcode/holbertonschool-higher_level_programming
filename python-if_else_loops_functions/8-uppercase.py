#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            new_str += "{}".format(chr(ord(i) - 32))
        else:
            new_str += "{}".format(i)
    print("{}".format(new_str))
