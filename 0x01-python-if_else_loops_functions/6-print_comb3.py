#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if j == 9 and i == j-1:
            print("{}{}".format(i, j))
        elif i != j:
            print("{}{}".format(i, j), end=', ')
