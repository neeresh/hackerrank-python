# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

string, size = input().split(" ")

sorted_string = ''.join(sorted(string.upper()))

for i in range(1, int(size)+1):
    for j in combinations(sorted_string, i):
        print("".join(j))
