#!/usr/bin/python3
def uppercase(str):
    for i in str:
        uppercase_char = chr(ord(i) & ~32)
        print("{}".format(uppercase_char), end='')
    print()
