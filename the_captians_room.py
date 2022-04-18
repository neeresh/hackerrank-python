# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

group_size = int(input())
room_numbers_list = list(input().split(" "))

counter_result = Counter(room_numbers_list)
search_value = min(counter_result.values())

for key, value in counter_result.items():
    if counter_result.get(key) == search_value:
        print(key)
