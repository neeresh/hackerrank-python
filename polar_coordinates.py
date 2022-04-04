# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

complex_number = complex(input())

for result in cmath.polar(complex_number):
    print(result)
