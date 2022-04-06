n = int(input())
s = set(map(int, input().split()))

number_of_commands = int(input())

for i in range(number_of_commands):
    user_input = input()

    if len(user_input.split(" ")) == 1:
        s.pop()
    else:
        command, value = user_input.split(" ")
        if command == "remove":
            s.remove(int(value))
        elif command == "discard":
            s.discard(int(value))

    # print(s)

print(sum(s))




