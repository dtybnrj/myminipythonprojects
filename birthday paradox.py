from random import *
from datetime import *
# for leap year finding code
# year=randint(1900,2999)
# print(year)
#
# if year%4==0 and year%100!=0 or year%400==0:
#     print("it is a leap year ")
# else:
#     print("it is not a leap year")

year=randint(1885,2017)
i=0
birthday=[]
i=0
while i<50:
    if year%4==0 and year%100!=0 or year%400==0:
        leap=1
    else:
        leap=0
    month=randint(1,12)
    if month==2 and leap==1:
        date=randint(1,29)
    elif month==2 and leap==0:
        date=randint(1,28)
    elif month%2!=0 and month<7:
        date=randint(1,31)
    elif month%2!=0 and month>7:
        date=randint(1,31)
    else:
        date=randint(1,30)

        dd=datetime.date(year,month,date)
        dayOfYear=dd.timetuple().tm_yday
        i=i+1
        birthday.append(dayOfYear)

i=0
while i<50:
    print(birthday[i])
    i=i+1
