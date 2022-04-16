def isAlnum(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;

def isAlpha(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False; 

def isDigit(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def isLower(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 

def isUpper(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;



if __name__ == '__main__':
    s = input()

    print(isAlnum(s))
    print(isAlpha(s))
    print(isDigit(s))
    print(isLower(s))
    print(isUpper(s))

    
