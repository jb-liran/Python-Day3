# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:52:03 2018

@author: jbt
"""

def fn(a,b,gn):
    gn(a)
    print("*************")
    gn(b)
    
    
def f4(val):
    print ("#" * val)

def f55(val):
    print ("$$" * val)
           

fn(10,5,f55)

