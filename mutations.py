def mutate_string(string, position, character):
    
    nameList = list(string)
    nameList[position] = character
    
    modifiedName = "".join(nameList)    
    
    return modifiedName

