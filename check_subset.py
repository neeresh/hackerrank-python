# Enter your code here. Read input from STDIN. Print output to STDOUT
numberOfTestCases = int(input())

for _ in range(numberOfTestCases):
    
    numberOfElementsInSetA = int(input())
    setA = input().split()
    
    numberOfElementsInSetB = int(input())
    setB = input().split()
    
    if all(number in setB for number in setA):
        print("True")
    else:
        print("False")






