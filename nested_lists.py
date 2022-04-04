if __name__ == '__main__':
    
    records = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records[name] = score
    
    names = records.keys()
    secondLowest = sorted(list(set(records.values())), reverse=False)[1]
    filteredNames = [name for name in names if records[name] == secondLowest]
    
    for name in sorted(filteredNames):
        print(name)
    
        
