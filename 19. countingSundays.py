"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

def leapYear(year):
    return(year%4==0 and ((year%100==0 and year%400==0)or(year%100!=0)))

month=[31,28,31,30,31,30,31,31,30,31,30,31]
leapMonth=[31,29,31,30,31,30,31,31,30,31,30,31]
count=0
day=0
for i in range(100):
    year=i+190
    if(leapYear(year)):
        useMonth=leapMonth
    else:
        useMonth=month
    for mon in month:
        for x in range(mon):
            day+=1
            if((day+1)%7==0 and x==0):
                count+=1
print(count)
