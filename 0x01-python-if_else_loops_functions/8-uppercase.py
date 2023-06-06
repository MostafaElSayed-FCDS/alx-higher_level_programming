#!/usr/bin/python3
def uppercase(s):
    for i in s:
        uppercase_char = chr(ord(i) & ~32)
        print(uppercase_char, end='')
