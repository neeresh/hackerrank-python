# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    boolean = True
    
    try:
        regex = re.compile(input())
    
    except re.error:
        boolean = False
    
    print(boolean)



