# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:45:39 2018

@author: jbt
"""

def simp():
    firstnum = 0
    while True:
        num = firstnum;
        while True:
            num+=10
            firstnum = yield num
            print("in while",firstnum)
            if firstnum:
                break
 
it=simp()
print(next(it)) 
print(next(it)) 
print(next(it)) 
 
print(it.send(200)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
