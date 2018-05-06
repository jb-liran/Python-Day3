# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:31:48 2018

@author: jbt
"""

a=90


def f1():
    """ sample function """
    global a
    a=100
    print("in f1",a)
    
def f2(v):
    """ function f2
        v - number of stars """
    global a
    print(a)
    print("hello")
    if v > 100:
        a=80

f2(120)
print(a)
f1()
f2(12)