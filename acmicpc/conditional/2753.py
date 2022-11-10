year = int(input())

cond_1 = year % 4 == 0 and year % 100 != 0
cond_2 = year % 400 == 0

print(1 if cond_1 or cond_2 else 0)

