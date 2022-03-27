# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_tests = int(input())

for i in range(number_of_tests):

    try:
        a, b = input().split(" ")
        print(int(int(a)/ int(b)))

    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code: {}".format(e))

    
