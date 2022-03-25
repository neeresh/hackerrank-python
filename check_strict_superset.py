# Enter your code here. Read input from STDIN. Print output to STDOUT

setA = input().split()

numberOfSets = int(input())

toCompare = []

for _ in range(numberOfSets):
    setB = input().split()
    toCompare.append(setB)

flag = True

for sett in toCompare:
    
    if all(number in setA for number in sett):
        pass
    else:
        flag = False
        break

print(flag)





