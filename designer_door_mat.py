# Enter your code here. Read input from STDIN. Print output to STDOUT

inputs = input().split(" ")
N, M = int(inputs[0]), int(inputs[1])


dash = '-'
dot = '.'
pipe = '|'
message ='WELCOME'

oddsForTopCone = [i for i in range(N) if i%2 != 0]
oddsForBottomCone = oddsForTopCone[::-1]

topConedashesToPrint = int((M-3)/2) # Top Cone
messageLength = len(message)

# Top Cone
for i in range(int(N/2)):
    print( (dash*(topConedashesToPrint - 3*i)) + ((dot + pipe + dot)*oddsForTopCone[i]) + (dash*(topConedashesToPrint - 3*i)) )

# Welcome Message
print( (dash*int((M - messageLength)/2)) + message + (dash*int((M - messageLength)/2)) )

# Bottom Cone
for i in range(int(N/2)):
    print( dash*int(int(M-(3*oddsForBottomCone[i]))/2) + ((dot + pipe + dot)*oddsForBottomCone[i]) + dash*int(int(M-(3*oddsForBottomCone[i]))/2) )
    
