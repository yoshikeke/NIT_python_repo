year = int(input())
month = int(input())
day = int(input())
def isLeepYear(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True

def YearDays(y):
    if isLeepYear(y):
        return 366
    else:
        return 365

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def MonthDays(y,m):
    result = days_in_month[m-1]
    if isLeepYear(y):
        if m == 2:
            result = result + 1
    return result

def DaysFromNewYears(y,m,d):
    days = 0
    for i in range(0,m-2):
        days = days + days_in_month[i]
    days = days + d
    if m > 2 and isLeepYear(y):
        days = days + 1
    return days

print(YearDays(year))
print(isLeepYear(year))
print(MonthDays(year,month))
print(DaysFromNewYears(year,month,day))
