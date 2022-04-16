set_a_size = int(input())
set_a = set(list(input().split(" ")))

number_of_other_sets = int(input())

for i in range(number_of_other_sets):
    command, length = input().split(" ")

    if command == "intersection_update":
        set_b = set(list(input().split(" ")))
        set_a.intersection_update(set_b)

    elif command == "update":
        set_b = set(list(input().split(" ")))
        set_a.update(set_b)

    elif command == "symmetric_difference_update":
        set_b = set(list(input().split(" ")))
        set_a.symmetric_difference_update(set_b)

    elif command == "difference_update":
        set_b = set(list(input().split(" ")))
        set_a.difference_update(set_b)

print(sum(map(int, set_a)))
