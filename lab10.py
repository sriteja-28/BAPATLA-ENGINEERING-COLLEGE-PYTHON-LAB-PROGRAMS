# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 09:05:41 2022

@author: y20acs507
"""

n=int(input("enter a number"))
for i in range(0,n+1):
    for j in range(i):
        print(i,end=" ")
    print()