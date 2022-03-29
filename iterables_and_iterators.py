from itertools import combinations

length_of_the_list = int(input())
english_letters = input().split(" ")
indices_to_be_selected = int(input())

count = 0
total = 0

for i in combinations(english_letters, indices_to_be_selected):
    count += 'a' in i
    total += 1

print(count/total)
