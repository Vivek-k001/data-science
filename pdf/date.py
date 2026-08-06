date1 = input("Enter the first date (day month year): ").split()
date2 = input("Enter the second date (day month year): ").split()

day1 = int(date1[0])
month1 = int(date1[1])
year1 = int(date1[2])

day2 = int(date2[0])
month2 = int(date2[1])
year2 = int(date2[2])

if (year1, month1, day1) > (year2, month2, day2):
    print("First date is later.")
elif (year1, month1, day1) < (year2, month2, day2):
    print("Second date is later.")
else:
    print("Both dates are the same.")
