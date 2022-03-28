if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    studentMarks = student_marks[query_name]
    
    average = sum(studentMarks) / len(studentMarks)
    
    print("{:0.2f}".format(average))
    
