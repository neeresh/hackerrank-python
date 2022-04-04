import numpy

coefficients = list(map(float, input().split()))
at_point = int(input())

print(numpy.polyval(coefficients, at_point))

