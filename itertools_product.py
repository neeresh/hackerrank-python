# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

cartesian_products = list(product(a, b))

for pair in cartesian_products:
    print(pair, end=" ")

