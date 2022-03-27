# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split(" "))

default_dict = defaultdict(list)

for i in range(1, n+1):
    default_dict[input()].append(i)

for j in range(1, m+1):
    key = input()

    if len(default_dict[key]) > 0:
        print(" ".join(str(k) for k in default_dict[key]))
    else:
        print(-1)

