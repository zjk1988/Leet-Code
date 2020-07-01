参考：
https://www.cnblogs.com/yjiyjige/p/3263858.html
https://blog.csdn.net/your_answer/article/details/79619406

def KMP(L,t):
    i = 0
    j = 0
    nexts = getnext(t)
    while (i<len(L) and j<len(t)):
        if L[i]==t[j] or j==-1:
            i = i+1
            j = j+1
        else:
            j = nexts[j]
    if j == len(t):
        return i-j
    else:
        return -1
def getnext(t):
    j = 0
    k = 0
    nexts = [0 for _ in range(len(t))]
    nexts[0] = -1
    for indx in range(len(t)-1) :#记得-1因为记录的是刚刚不匹配的点的
        if indx==-1 or nexts[j]==nexts[k]:
            j = j+1
            k = k+1
            nexts[j] = k
        else:
            k = nexts[k]
    return nexts
        
KMP('12343232','343')        
    
getnext('aaaaas')    
