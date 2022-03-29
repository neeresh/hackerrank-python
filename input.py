# Enter your code here. Read input from STDIN. Print output to STDOUT

x1, k = input().split()

poly = input()

result = poly.replace('x', x1)

if eval(result) == int(k):
    print(True)
else:
    print(False)

