# Enter your code here. Read input from STDIN. Print output to STDOUT


user_input = list(input())

lower_case = []
upper_case = []
evens = []
odds = []

for i in user_input:
    if i.islower():
        lower_case.append(i)
    elif i.isupper():
        upper_case.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

print(''.join(sorted(lower_case) + sorted(upper_case) + sorted(odds) + sorted(evens)))

