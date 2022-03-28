if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sortedArray = sorted(list(set(arr)), reverse=True)
    
    print(sortedArray[1])
    
