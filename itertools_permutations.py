# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

string, size = input().split(" ")

sorted_string = ''.join(sorted(string.upper()))

for pair in list(permutations(sorted_string, int(size))):
    print(''.join(pair))
