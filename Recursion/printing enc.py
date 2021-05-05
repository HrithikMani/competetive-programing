s = "12345"
ans = ""
def fun(s,ans):
    if(len(s) == 0):
        print(ans)
        return
    elif(len(s) == 1):
        x = s[0]
        if(x == "0"):
            return
        else:
            ch = chr(ord('a') + int(x) -1)
            print(ans+ch)
    else:
        x = s[0]
        y = s[1::]
        
        if(x == "0"):
            return
        else:
            ch = chr(ord('a') + int(x) -1)
            fun(y,ans+ch)
            x = int(s[0:2])
            y = s[2::]
            if(x<26):
                ch = chr(ord('a') + x -1)
                fun(y,ans+ch)
    
    
fun(s,ans)