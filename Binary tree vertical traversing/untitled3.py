# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:58:58 2021

@author: hrith
"""


def fun(s,n,pos,opn,close):
    if(close == n):
        for i in s:
            print(i,end="")
        print()
        return 
    else:
        if(opn > close):
            s[pos] = "}"
            fun(s,n,pos+1,opn,close+1)
        if(opn<n):
            s[pos] = "{"
            fun(s,n,pos+1,opn+1,close)
    
n=3
s =[""] * 2 * n;
print(fun(s,n,0,0,0))    
y = 3


x=True
y= False


