#!/usr/bin/python3
s = ""
for i in range(122, 96, -1):
    if i % 2 != 0:
        s += chr(i-32)
    else:
        s += chr(i)
print("{}".format(s), end="")
