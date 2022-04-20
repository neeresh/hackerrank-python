import numpy

numbers = list(map(int, input().split()))


print(numpy.zeros((numbers), dtype=int))
print(numpy.ones((numbers), dtype=int))

