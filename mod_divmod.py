# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())

quotient_remainder = divmod(a, b)
print(quotient_remainder[0])
print(quotient_remainder[1])
print(quotient_remainder)
