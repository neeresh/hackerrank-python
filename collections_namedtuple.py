from collections import namedtuple

total_number_of_students = int(input())

student_details = namedtuple('student_details', input().split())

student_rows = list()
marks = list()

for i in range(total_number_of_students):
    student_rows.append(input().split())

for row in student_rows:
    get_marks = student_details._make(row)
    marks.append(int(get_marks.MARKS))

print(round(sum(marks)/total_number_of_students, 2))
