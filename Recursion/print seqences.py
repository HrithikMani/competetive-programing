# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:43:46 2021

@author: hrith
"""


a = "abc"
def fun(a,ans):
    if(len(a) == 0):
        print(ans)
    
    
    for i in range(len(a)):
        ch = a[i]
        left =  a[0:i]
        right = a[i+1::]
        r = left + right
        #print("LftPart => " +left+" Right Part => "+right)
        fun(r,ans+ch)
    
fun(a,"")