from itertools import product


def maximize_it(combination_tuple, modulus):
    # print(modulus)
    # print(sum(pow(int(i), 2) for i in combination_tuple) % modulus)

    return (sum(pow(int(i), 2) for i in combination_tuple)) % modulus


number_of_lists, modulus = input().split(" ")
user_lists = list()

result_dict = {}

for i in range(int(number_of_lists)):
    user_lists.append(input().split(" ")[1:])
    # print(user_lists[i])

# print(list(product(*user_lists)))
# maximize_it(('5', '9', '10'), int(modulus))

# print(user_lists)

for each_tuple in set(list(product(*user_lists))):
    result_dict[each_tuple] = maximize_it(each_tuple, int(modulus))

# print(result_dict)
print(max(result_dict.values()))
