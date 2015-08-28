#!/usr/bin/env python
#coding=utf-8
#from __future__ import division  
  
def jia(x,y):
    print(x+y)  
            
def jian(x,y):
    print(x-y)  
                      
def cheng(x,y):
    print(x*y)
                                
def chu(x,y):
    print(x/y)
                                          
operator = {'+':jia,'-':jian,'*':cheng,'/':chu}  
                                            
operator['+'](5,5)  
