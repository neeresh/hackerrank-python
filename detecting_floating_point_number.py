# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

number_of_inputs = int(input())

pattern = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')

for _ in range(number_of_inputs):
     user_input = input()
     
    #  print(user_input)
    #  print(re.search(pattern, user_input))
     
     if pattern.match(user_input):
        print(True)
     else:
        print(False)
     



