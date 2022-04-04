# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split(" "))
integers_array = list(map(int, input().split(" ")))
like_set = set(map(int, input().split(" ")))
dislike_set = set(map(int, input().split(" ")))

happiness = 0

for i in integers_array:
    if i in like_set:
        happiness = happiness + 1
    elif i in dislike_set:
        happiness = happiness - 1

print(happiness)
