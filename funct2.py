# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:41:24 2018

@author: jbt
"""

#def str(a):
#    print("a")

def fout(a):
    
    def fin(b):
        print ("*" * b)
    
    fin(a)
    print("hello")
    fin(a*2)
    
fout(10)