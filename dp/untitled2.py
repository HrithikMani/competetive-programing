def fun(n):
    if(n==0):
        return [""]
    elif(n<0):
        return []
    path1 = fun(n-1)
    path2 = fun(n-2)
    path3 = fun(n-3)
    paths = []
    for x in path1:
        paths.append("1"+x)
    for y in path2:
        paths.append("2"+y)
    for z in path3:
        paths.append("3"+z)
    return paths


n = 4
print(fun(n))