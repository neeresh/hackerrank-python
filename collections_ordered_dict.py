# Enter your code here. Read input from STDIN. Print output to STDOUT


from collections import OrderedDict

number_of_items = int(input())
ordered_dict = OrderedDict()

for items in range(number_of_items):
    name_price = input().split(" ")
    price = name_price.pop(-1)
    name = ' '.join(name_price)

    if name in ordered_dict.keys():
        ordered_dict[name] = int(ordered_dict.get(name)) + int(price)
    else:
        ordered_dict[name] = price

for key, value in ordered_dict.items():
    print(key, value)

