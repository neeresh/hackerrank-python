# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_country_stamps = int(input())

country_stamps = set()

for i in range(number_of_country_stamps):
    country_stamps.add(input())
    
print(len(country_stamps))

