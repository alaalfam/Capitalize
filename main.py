#!/bin/python

import math
import os
import random
import re
import sys


def solve(s):
    list = s.split(" ")
    s = ""
    for i in list:
        if i == "":
            s += " "
        else:
            s += i[0].upper()
            for j in range(1, len(i)):
                s += i[j]
            s += " "
    return s


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
