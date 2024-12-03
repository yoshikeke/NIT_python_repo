print("start day")
year = int(input())
month = int(input())
day = int(input())
print("end day")
end_year = int(input())
end_month = int(input())
end_day = int(input())

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

def daysDistance(y,m,d,ey,em,ed):
    result = 0
    days = DaysFromNewYears(y,m,d)
    end_days = DaysFromNewYears(ey,em,ed)
    if ey-y > 0 :
        for i in range(1,ey-y):
            result += YearDays(ey-i)
        result += YearDays(y) - days + end_days   
    else :
        result = end_days - days
    return result




