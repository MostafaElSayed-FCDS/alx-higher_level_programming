#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(c) >= 97 and ord(c) <= 122:
            i = chr(ord(i) & ~32)
        print("{}".format(i), end='')
    print()
