def swap_case(s):
    
    finalWord = []
    
    for i in s:
        if i.islower():
            i = i.upper()
            finalWord.append(i)
        elif i.isupper():
            i = i.lower()
            finalWord.append(i)
        else:
            finalWord.append(i)
            pass
    
    result = ''.join(finalWord)
    
    return result

