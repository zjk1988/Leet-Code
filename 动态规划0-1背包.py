N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
def bag(N,W,wt,val):
    import numpy as np
    dp = np.zeros((N+1,W+1))
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j-wt[i-1]>0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][W]
bag(N,W,wt,val)
