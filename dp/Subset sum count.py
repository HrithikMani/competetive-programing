# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:56:00 2021

@author: hrith
"""
import numpy as np
a = [1,2,3]

n = 5

p = np.array([[-1 for i in range(n+1)] for j in range(len(a)+1)])

def fun2(a,n,s):
    if(s == 0):
        return 1
    if(n == 0):
        return 0
    if(p[n][s] != -1):
        return p[n][s]
    if(a[n-1] <= s):
        p[n][s] = fun2(a,n-1,s-a[n-1]) + fun2(a,n-1,s)
        return p[n][s]
    else:
        p[n][s] = fun2(a,n-1,s)
        return p[n][s]

print(p)
print(fun2(a,len(a),n))




def fun(a,n,s):
    if(s == 0):
        return 1
    if(n == 0):
        return 0
    if(a[n-1] <= s):
        return fun(a,n-1,s-a[n-1]) + fun(a,n-1,s)
    else:
        return fun(a,n-1,s)

def fun1(a,n,s):
    
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    for j in range(n+1):
        dp[j][0] = 1
    for i in range(1,n+1):
        for j in range(1,s+1):
            if(a[i-1] <= j):
                dp[i][j] = dp[i-1][j-a[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
        print(np.array(dp))
    return dp[n][s]

print(fun1(a,len(a),n))