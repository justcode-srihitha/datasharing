#!/usr/bin/env python
# coding: utf-8

import sys
#sys.path.insert(0, './my_proj_env/')
import gps_health_daily

def test_add_sub():
    print('Hey')
    add,sub = gps_health_daily.add_sub_actual()
    print(add,sub)

def justlykthat():
    print('simply')

#calling funtions


test_add_sub()
justlykthat()


def test_multiply(a,b):
    gps_health_daily.multiply_fun(a,b)
    
test_multiply(5,2)
    
