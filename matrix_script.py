#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(list(matrix_item))

# print(matrix)

matrix_message = []

for i in zip(*matrix):
    matrix_message.append(''.join(i))

matrix_message = ''.join(list(''.join(matrix_message)))

# print(matrix_message)
print(re.sub(r"(?<=\w)([^\w\d]+)(?=\w)", " ", matrix_message))
