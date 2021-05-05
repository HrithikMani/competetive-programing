# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:03:26 2021

@author: hrith
"""
'''
to count number of ways in which we can find number coins to form s (not minimum) we 
should simply find subset sum for s

    25
    30 -10 = 20
    20 - 10 10
    
    1 -> 10 10 10 
    

'''
import sys
a = [25,10,5]
s = 30
n=len(a)
#recursive
def fun1(a,s,n):
    if(n==0 and s==0):
        return 0
    if(s == 0):
        return 0
    if(n==0):
        return sys.maxsize
    
    
    
    if(a[n-1] <= s):
        return min(1+ fun1(a,s-a[n-1],n),fun1(a,s,n-1))
    else:
        return  fun1(a,s,n-1)




print(fun1(a,s,n))
#dp
def fun(a,s):
    n=len(a)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(1,s+1):
        dp[0][i] = sys.maxsize 
    for i in range(1,s+1):
        if(i%a[0] == 0):
            dp[1][i] = i//a[0]
    for i in range(2,n+1):
        for j in range(1,s+1):
            if(a[i-1]<=j):
                dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-a[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][s])
#fun(a,s)