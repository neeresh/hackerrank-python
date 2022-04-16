# Enter your code here. Read input from STDIN. Print output to STDOUT

english_paper_students = int(input())
english_students_rollnumbers = list(map(int, input().split(" ")))

french_paper_student = int(input())
french_students_rollnumbers = list(map(int, input().split(" ")))


print(len(set(english_students_rollnumbers).union(set(french_students_rollnumbers))))



