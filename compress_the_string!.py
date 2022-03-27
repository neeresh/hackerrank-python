# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

string = input() # 1222311

for key, group in groupby(string):
    print((len(list(group)), int(key)), end=' ')
