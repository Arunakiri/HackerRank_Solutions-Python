#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr_sorted = sorted(arr, key=lambda x:x[k])
    
    for lis in arr_sorted:
        print(' '.join([str(i) for i in lis]))
            
