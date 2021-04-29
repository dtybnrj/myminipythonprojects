# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:59:41 2019

@author: adity
"""
import calendar
def check_leap_year(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False
        
def check_the_date(d,m,y,l):
    if l:
        if m==2:
            if d<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
            else:
                 if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False
                 else:
                    if d<31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if d<29:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
            else:
                 if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False
                 else:
                    if d<31:
                        return True
                    else:
                        return False
        
def get_day(day_index):
    day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    return day[day_index]

while(1):
    year=int(input("Enter the year from 1970: "))
    if year<1970:
        print("please enter the valid year starting from 1970")
        
    else:
        break
while(1):    
    month=int(input("Enter the month: "))
    if month<=12 and month>0:
        break
    else:
        print("Enter the valid month from 1-12")
        
leap=check_leap_year(year)

while(1):
    date=int(input("enter the date: "))
    if date>0 and check_the_date(date,month,year,leap):
        break
    else:
        print("Enter the a valid date")
        
day_index=calendar.weekday(year,month,date)
day=get_day(day_index)
print(day)