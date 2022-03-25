# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import Counter

number_of_shoes = int(input()) # 10
shoe_sizes_available = input().split(" ") # 2 3 4 5 6 8 7 6 5 18
number_of_customers = int(input()) # 6

total_available_sizes = Counter(shoe_sizes_available)

# print(total_available_sizes)

total_cost = 0

for customer in range(0, number_of_customers):
    shoe_size, dollars = input().split(" ")

    if shoe_size in total_available_sizes.keys() and total_available_sizes.get(shoe_size) > 0:
        total_available_sizes[shoe_size] = total_available_sizes.get(shoe_size) - 1
        total_cost = total_cost + int(dollars)

print(total_cost)
