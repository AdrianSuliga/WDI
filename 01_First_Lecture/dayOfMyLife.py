import math

day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

cDay = int(input("Enter current day: "))
cMonth = int(input("Enter current month: "))
cYear = int(input("Enter current year: "))

daysOfMyLife = 0
daysInCMonth = 0

#count days in birth year
#count days in current month
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    daysInCMonth = 31 - day + 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    daysInCMonth = 30 - day + 1
elif month == 2 and year%4 == 0:
    daysInCMonth = 29 - day + 1
elif month == 2 and year%4 != 0:
    daysInCMonth = 28 - day + 1

daysOfMyLife += daysInCMonth

#count remaining days in a year
month += 1
while month <= 12:
    if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        daysInCMonth = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        daysInCMonth = 30
    elif month == 2 and year%4 == 0:
        daysInCMonth = 29
    elif month == 2 and year%4 != 0:
        daysInCMonth = 28
    daysOfMyLife += daysInCMonth
    month += 1

#count days in full years
year = year + 1
while year < cYear:
    if (year % 4 == 0):
        daysOfMyLife += 366
    else:
        daysOfMyLife += 365
    year += 1

#count days in current year excluding current month
counter = 1
while counter < cMonth:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        daysInCMonth = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        daysInCMonth = 30
    elif month == 2 and year%4 == 0:
        daysInCMonth = 29
    elif month == 2 and year%4 != 0:
        daysInCMonth = 28
    daysOfMyLife += daysInCMonth
    counter += 1

daysOfMyLife += cDay

print(daysOfMyLife)
print("FACTORISATION:")

b = 2
while b <= math.sqrt(daysOfMyLife):
    if (daysOfMyLife % b == 0):
        print(b, end=' ')
        daysOfMyLife = daysOfMyLife // b
    else:
        b+=1
if daysOfMyLife > 1: print(daysOfMyLife)