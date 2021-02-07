#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.split(' ')
    new_l = []
    for word in l:
        if word is not '':
            new_l.append(word[0].upper()+word[1:])
        else:
            new_l.append(word)
    return ' '.join(new_l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
