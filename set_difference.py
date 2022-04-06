# Enter your code here. Read input from STDIN. Print output to STDOUT

english_subscription = int(input())
english_students_rollnumbers = list(map(int, input().split(" ")))

french_subscription = int(input())
french_students_rollnumbers = list(map(int, input().split(" ")))

print(len(set(english_students_rollnumbers).difference(set(french_students_rollnumbers))))

