

# Complete the solve function below.
# Complete the solve function below.
def solve(s):
    
    sList = s.split(" ")
    result = []

    for i in sList:
        if i.isalpha():
            result.append(i.capitalize())
        else:
            result.append(i)
    
    return " ".join(result)

