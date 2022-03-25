# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

inputs = int(input())

d = deque()

for i in range(inputs):
    command = input().split(" ")
    
    if len(command) > 1:
        value = command.pop()
    
    command = command[0]
    
    if command == "append":
        d.append(int(value))
    elif command == "appendleft":
        d.appendleft(int(value))
    elif command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
    
for i in d:
    print(i, end=' ')
