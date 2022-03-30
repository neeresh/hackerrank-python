if __name__ == '__main__':
    N = int(input())
    
    commands = []
    
    for i in range(N):
        command = input().split()
        commands.append(command)
    
    # print(commands)
    
    finalList = []
    
    for command in commands:
        
        if "insert" in command:
            _, index, value = command
            finalList.insert(int(index), int(value))
        elif "print" in command:
            print(finalList)
        elif "remove" in command:
            _, value = command
            finalList.remove(int(value))
        elif "append" in command:
            _, value = command
            finalList.append(int(value))
        elif "sort" in command:
            finalList = sorted(finalList)
        elif "pop" in command:
            finalList.pop()
        elif "reverse" in command:
            finalList.reverse()
        
        
     
    
    
