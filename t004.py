#coding=utf-8
#输入某年某月某日，判断这一天是这一年的第几天？

daySum = 0
year = int(raw_input("year:"))
month = int(raw_input("month:"))
day = int(raw_input("day:"))

list31 = {1,3,5,7,8,10,12}
list30 = {4,6,9,11}
def isLeap(year):
    '''判断某一年是否为闰年，闰年返回1平年返回0'''
    leap = 0
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 == 0:
                leap = 1
            else:
                leap = 0
        else:
            leap = 1
    else:
        leap = 0
    return leap
    
for monthidx in range(1,month):
    if(monthidx in list31):
        daySum+=31
    if(monthidx in list30):
        daySum+=30
    if(monthidx == 2):
        daySum = daySum + 27 + isLeap(year)
daySum+=day

print(isLeap.__doc__)

print('这是一年中的第{}天'.format(daySum))

