# Enter your code here. Read input from STDIN. Print output to STDOUT
english_subscription = int(input())
english_rollnumbers = list(map(int, input().split(" ")))

french_subscription = int(input())
french_rollnumbers = list(map(int, input().split(" ")))

print(len(set(english_rollnumbers).intersection(set(french_rollnumbers))))

