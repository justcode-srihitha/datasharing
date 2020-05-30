#!/usr/bin/env python
# coding: utf-8

import math

class Addition_subtraction(object):
    def __init__(a,s):
        self.a = a
        self.s = s
 
def add_sub_actual()->Addition_subtraction:
    x=9
    y=10
    a=x+y
    s=abs(x-y)
    print('HI')
    return (a,s)
        
    
def multiply_fun(x,y):
    c=x*y
    print(c)

def string_add(str1,str2):
    return " ".join([str1,str2])
