参考：
https://www.cnblogs.com/yjiyjige/p/3263858.html
https://blog.csdn.net/your_answer/article/details/79619406
上面两个博客稍微有点错误，就是不匹配的时候会出不去循环
def KMP(s1,s2):
    next_arr = next_array(s2)
    i = 0
    j = 0
    l1 = len(s1)
    l2 = len(s2)
    while (i<l1 and j<l2):
        if j==-1 or s1[i]==s2[j]:
            
            j+=1
        else:
            j = next_arr[j]
        i+=1
    if j == l2:
        return i-j
    else:
        return -1
def next_array(s):
    l = len(s)
    nexts = [0 for _ in range(l)]
    nexts[0] = -1
    j=0
    k=0
    while j<l:
        if (k==-1 or nexts[j]==nexts[k]):
            k = k+1
            j = j+1
            nexts[j] = k
        else:
            k = nexts[k]
        j = j+1
    return nexts
KMP("hfllo",'ll')
 
