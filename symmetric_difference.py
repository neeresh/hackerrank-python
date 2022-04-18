# Enter your code here. Read input from STDIN. Print output to STDOUT


set_m = int(input())
set_m_values = set(map(int, input().split(" ")))

set_n = int(input())
set_n_values = set(map(int, input().split(" ")))

symmetric_difference = list(set_m_values.difference(set_n_values)) + list(set_n_values.difference(set_m_values))

for value in sorted(symmetric_difference):
    print(value)

