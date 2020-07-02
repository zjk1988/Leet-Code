#    自顶向下的递归方法
def integerBreak(n):
    if n==1:
        return 1
    re = -1
    for i in range(1,n):
        re = max(re,i*(n-i),i*integerBreak(n-i))
    return re
integerBreak(10)    
    
    
    
#自顶向下的记忆化搜索 有问题
def   integerBreak(n):
    global re
    re =  [-1]*(n+1)
    if n==1:
        return 1
    if re[n]!=-1:
        return re[n]
    res = -1
    for i in range(1,n):
        res = max(res,i*(n-i),i*integerBreak(n-i))
    print(res)
    re[n] = res
    
    return res
integerBreak(10)  
        
动态规划    
def integerBreak(n):
    global re
    re =  [-1]*(n+1)
    re[1] = 1
    for i in range(2,n+1):
        for j in range(1,i):
            re[i] = max(re[i],j*(i-j),j*re[i-j])
    return re[n]
integerBreak(10)      
