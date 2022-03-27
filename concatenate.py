import numpy

N, M, P = list(map(int, input().split(" ")))

NP_array = []
MP_array = []

for _ in range(N):
    NP_array.append(list(map(int, input().split())))


for _ in range(M):
    MP_array.append(list(map(int, input().split())))

NMP_array = numpy.concatenate((NP_array, MP_array))

print(NMP_array)
