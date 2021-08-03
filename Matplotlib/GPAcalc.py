#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:56:35 2018

@author: AlexClevenger

"""
grades=[]
x=0;
numc=input("How many classes are you taking? ")
numclass=int(numc)
for x in range(numclass):
    n=0;
    result=input("Class: ")
    grade= input("Grade: ")
    if(grade=="A+" or grade=="a+"):
        n= (13/3)
    if(grade=="A" or grade=="a"):
        n=4.0
    if(grade=="A-" or grade=="a-"):
        n=(11/3)
    if(grade=="B+" or grade=="b+"):
        n= (10/3)
    if(grade=="B" or grade=="b"):
        n=3.0
    if(grade=="B-" or grade=="b-"):
        n=(8/3)
    if(grade=="C+" or grade=="c+"):
        n=(7/3)
    if(grade=="C" or grade=="c"):
        n=2.0
    honors= input("Honors or AP? (yes/no) "+ '\n')
    if(honors=="Yes" or honors=="yes"):
        n+=(2/3)
    grades.append(n)
GPA=0
i=0
for i in range(len(grades)):
    GPA+=grades[i]
GPA/=numclass

print("Your GPA is "+ str(GPA))
    
    
