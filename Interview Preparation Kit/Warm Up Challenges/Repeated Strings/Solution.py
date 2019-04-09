#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) == 1:
        if s == 'a':
            return n
        else:
            return 0
    l = s.count('a')
    c = math.floor(n/len(s))
    res = l*c
    res += s[:(n%len(s))].count('a')
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
