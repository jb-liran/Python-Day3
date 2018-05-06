# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def addmul(a,b):
    return [a+b,a*b]

def add(a,b):
    return a*10+b
    
def addall(a,b,*args):
    print (args)
    
    
def prinall(**args):
    print(args)
    
def genfn(*args, **kargs):
    print(args)
    print(kargs)
    
x = add(b=20,a=90)


d1={'user': 'liran', 'password': 1234, 'db': 'abc'}


#print(x)