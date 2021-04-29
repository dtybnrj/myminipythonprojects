# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:42:03 2019

@author: adity
"""
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    def __init__(self,fname,lname,year):
        Person.__init__(self,fname,lname)
        self.graduation=year
        Person.printname(self)
        print(self.graduation)
x=Student("aditya","banerjee",2021)
x.__init__