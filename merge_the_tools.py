from collections import OrderedDict

def merge_the_tools(string, k):
    n = len(string) # 9

    substrings_dict = OrderedDict()

    for i in range(0, n, k):
        print(''.join(substrings_dict.fromkeys(string[i:i+k])))

