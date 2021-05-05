# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:41:22 2021

@author: hrith

122

1 22
     2 
         2

1 1111
   1  111
       1     11 
              1    1
                      




                    1
                        2
1 + (2 + 2)
2  +  (1 + (1 + (1)))

"""
def fun(k):
    
    if(k == 0):
        return [""]
    if(k<0):
        return []
    
    
    path1= fun(k-5)
    path2 = fun(k-25)
    path3 = fun(k-3)
    
    paths = []
    for i in path1:
        paths.append(str(1) + i)
    for i in path2:
        paths.append(str(2) + i)
    for i in path3:
        paths.append(str(3) + i)
    return paths
        
    

k = 5
print(fun(5))