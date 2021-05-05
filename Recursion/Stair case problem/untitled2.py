def fun(n):
    if(n == 0):
        return [""]
    if(n<0):
        return []
    
    
    path1 = fun(n-1)
    path2 = fun(n-2)
    path3 = fun(n-3)
    
    paths = []
    
    for p in path1:
        x = str(1) + p
        paths.append(x)
    for i in path2:
        x = str(2) + i
        paths.append(x)
    for i in path3:
        x = str(3) + i
        paths.append(x)
    return paths




n = 8;
print(fun(n)) 
        
        