# Enter your code here. Read input from STDIN. Print output to STDOUT

no_of_students, number_of_subjects  = list(map(int, input().split()))

marks = list()

for _ in range(number_of_subjects):
    marks.append(list(map(float, input().split())))

for i in zip(*marks):
    print(round(sum(i)/number_of_subjects, 1))
