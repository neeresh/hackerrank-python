# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

string, size = input().split(" ")

sorted_string = ''.join(sorted(string.upper()))

for pair in list(combinations_with_replacement(sorted_string, int(size))):
    print(''.join(pair))
