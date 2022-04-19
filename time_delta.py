#!/bin/python3

import math
import os
import random
import re
import sys
import dateutil.parser

# Complete the time_delta function below.
def time_delta(t1, t2):
    date1 = dateutil.parser.parse(t1, fuzzy=True)
    date2 = dateutil.parser.parse(t2, fuzzy=True)
    
    difference = date2 - date1
    
    return str(abs(int(difference.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
