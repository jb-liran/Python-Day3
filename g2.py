# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:44:17 2018

@author: jbt
"""

def withgen(num):
    i=0;
    while True:
        i+=1
        yield i
 
s=withgen(10);
print (s)
 
for i in s:
    print(i)