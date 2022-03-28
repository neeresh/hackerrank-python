import math

length_of_AB = int(input())
length_of_BC = int(input())


A = (length_of_BC, 0)
B = (0, 0)
D = (0, length_of_AB)
C = ((D[0]+A[0])/2, (D[1]+A[1])/2) # midpoint

# print(A, B, C, D)

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

print(str(round(getAngle(A, B, C))) + u"\N{DEGREE SIGN}")



