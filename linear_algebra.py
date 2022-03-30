import numpy

number_of_lines = int(input())

matrix = list()

for line in range(number_of_lines):
    matrix.append(list(map(float, input().split())))


print(round(numpy.linalg.det(matrix), 2))
