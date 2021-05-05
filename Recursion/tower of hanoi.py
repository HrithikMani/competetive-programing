# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:54:21 2021

@author: hrith
 we r moving a -> b using c
 
 left calls => a to c using b
 
 
 right call => c to b using a 



"""
def fun(n,a,b,c):
    if(n==0):
        return
    fun(n-1,a,c,b)
    print(str(n)+" [ "+a+"=>"+b+" ] ")
    fun(n-1,c,b,a)
print(fun(5,"1","2","3"))