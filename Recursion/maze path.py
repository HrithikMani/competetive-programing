# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:04:27 2021

@author: hrith
"""
a = [[0,0,0],[0,0,0],[0,0,0]]
ans=""
def fun(a,sr,sc,dr,dc,ans):
    if(sr>dr or sc >dc):
        return
    if(sr == dr and sc==dc):
        print(ans)
        return
    
    fun(a,sr+1,sc,dr,dc,ans+"v")
    fun(a,sr,sc+1,dr,dc,ans+"h")



fun(a,0,0,2,2,ans)
