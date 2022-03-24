# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_integers = int(input())

integers = list(map(int, input().split()))

flag = True

if all(number > 0 for number in integers):
    
    for i in  integers:
        if list(str(i)) == list(str(i))[::-1]:
            flag = False
            print(True)
            break
     
if flag:
    print(False)

    



