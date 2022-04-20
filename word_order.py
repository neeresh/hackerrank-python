# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

number_of_words = int(input())

words_list = list()

for i in range(number_of_words):
    words_list.append(input())

print(len(set(words_list)))

for count in Counter(words_list).values():
    print(str(count), end=" ")

