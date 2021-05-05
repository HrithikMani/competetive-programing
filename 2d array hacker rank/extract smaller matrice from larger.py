# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:50:30 2019

@author: hrith
"""
import numpy as np

def fun(m,x,y):
    slice_x = x
    slice_y =y
    width = len(m[0])
    height = len(m)
    slices = []
    for i in range(0, height - slice_y + 1):
        for j in range(0,width - slice_x + 1):
            slices.append(
                    [
                            [m[a][b] for b in range(j,j+slice_x)]
                            for a in range(i,i+slice_y)
                    ]
                    )
    return slices
    
    

a = np.random.randint(0,11,size=(6,6))    
print(a)
b = fun(a,3,3)
k =0
for s1 in b:
    for row in s1:
        print(row)
    k = k + 1
    print("--------")
print(k)    