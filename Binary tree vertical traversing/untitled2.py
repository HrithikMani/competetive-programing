a = [1,2,5]
k = 5
'''
5  -> 1 1 1 1 1
    -> 1 1 2 1


'''
#dp = [[-1 for i in range(k+1)]for j in range(len(a) +1) ]
#print(dp)
dp ={}
def fun(a,n,k,dp):
    if(n == 0):
        return 0
    if(k==0):
        return 1
    
    if(a[n-1] in dp.keys()):
        return dp[n-1]
    
    if(a[n-1] <= k):
         dp[n-1] = fun(a,n,k-a[n-1],dp) + fun(a,n-1,k,dp)
         #print(dp)
         return dp[n-1]
    else:
        dp[n-1] =  fun(a,n-1,k,dp)
        return dp[n-1]

print(fun(a,len(a),k,dp))