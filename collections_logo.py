#!/bin/python3
from collections import Counter  
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

    given_string = list(s)
    
    counted_dict = Counter(given_string)

    keys = sorted(set(counted_dict.keys()))
    values = sorted(list(counted_dict.values()), reverse=True)[0: 3]

    pointer = 0

    for i in range(len(values)):
        for j in keys:
            if counted_dict.get(j) == values[i]:
                print(j, values[i])
                keys.remove(j)
                break

