# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

vowels_list = re.findall(r'(?<=[^a^e^i^o^u])([aeiou]{2,})(?=[^a^e^i^o^u])', input(), re.IGNORECASE)

if len(vowels_list) > 0:
    for i in vowels_list:
        print(i)

else:
     print(-1)   











