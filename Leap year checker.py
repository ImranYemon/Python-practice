# determine if a year is leap year (leap is divisible by 4 but not by 100 unless also divisible by 400)

year =  int(input("year: "))

if (year%400 == 0) or (year%4 == 0 and year %100 != 0) :
    print(f" Year {year} is a leap year . ")
else  :
    print(f" Year {year} is not a leap year . ")

