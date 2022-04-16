# Enter your code here. Read input from STDIN. Print output to STDOUT

english = int(input())
english_students_rollnumbers = list(map(int, input().split(" ")))

french = int(input())
french_students_rollnumbers = list(map(int, input().split(" ")))

print(len(set(english_students_rollnumbers).symmetric_difference(set(french_students_rollnumbers))))

