# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, day, year = input().split()

dayIndexed = calendar.weekday(year=int(year), month=int(month), day=int(day))

print(list(calendar.day_name)[dayIndexed].upper())
