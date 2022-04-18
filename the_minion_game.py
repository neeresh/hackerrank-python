def minion_game(string):
    # your code goes here
    
    kevinScore = 0;
    stuartScore = 0;
    
    stringLength = len(string)
    
    for i in range(stringLength):
        if string[i] in "AEIOU":
            kevinScore += (stringLength)-i
        else :
            stuartScore += (stringLength)-i
    
    if kevinScore > stuartScore:
        print("Kevin", kevinScore)
    elif kevinScore < stuartScore:
        print("Stuart",stuartScore)
    else :
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)