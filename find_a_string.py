def count_substring(string, sub_string):
    
    subStringLength = len(sub_string)
    
    count = 0
    for i in range(0, len(string)):
        if string[i:i+subStringLength] == sub_string:
            count = count + 1
    
    return count

