1、冒泡排序

考虑外层循环，需要len-1次（最后一个元素就不用再走一次循环），外层循环i次也就是排序好了i个元素，考虑内层循环需要len-i-1次循环（同，最后一个元素就不用再走一次循环）

def bubble(L):
    l = len(L)
    for i in range(l-1):
        for j in range(l-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    print(L)
优化1：

如果内层循环某次没有交换数据，说明已经排好序了，设置一个标志位flag如果标志没动就结束排序

    l = len(L)
    flag = 0
    for i in range(l-1):
        for j in range(l-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                flag = 1
        if flag==1:
            break
    print(L)
优化2：

内层循环走完一次，最后交换点记为k，那么k之后的数据都是排好的，所以下一次的内层循环走到k就好

def bubble(L):
    l = len(L)
    flag = 0
    k = l-1
    for i in range(l-1):
        for j in range(k):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                flag = 1
        if flag==1:
            break
    print(L)
优化3：

对于数组这种可以随机访问的，可以正向走，也可以逆向走，所以，一次外层循环中可以正着走把大的放后，反向走把小的放前，反向走是从k位置走到第一位（从第0位开始算起）

def bubble(L):
    l = len(L)
    flag = 0
    k = l-1
    for i in range(l-1):
        for j in range(k):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                flag = 1
        if flag==1:
            break
        for t in range(k,0,-1):
            if L[t]<L[t-1]:
                L[t],L[t-1] = L[t-1],L[t]
    print(L)
2、选择排序

每次选择未排序的部分的最小值放到未排序部分的第一个位置

def selectionsort(L):
    l = len(L)
    for i in range(l-1):
        minindx = i
        for j in range(i+1,l):
            if L[j]<L[minindx]:
                minindx = j
        L[minindx],L[i] = L[i],L[minindx]
    print(L)
优化：

每次内层循环的时候不只是找min顺便把max也找了，但是内层循环找到本次的最大最小值之后不能简单地交换位置，因为会出现最大值在left的情况，这样再交换最大和right的时候把最小值放到right位置去了，所以要判断一下最大值是否在left，如果在找到新的max位置，也就是和left交换后的min位置，最后交换max和right的值

def selectionsort(L):
    l = len(L)
    left = 0
    right = l-1
    while left<right:
        minindx = left
        maxindx = right
        for j in range(left,right+1):
            if L[minindx]>L[j]:
                minindx = j
            if L[maxindx]<L[j]:
                maxindx = j
        temp = L[minindx]
        L[minindx],L[left] = L[left],L[minindx]
        if  left == maxindx:   
            maxindx = minindx
        L[maxindx],L[right] = L[right],L[maxindx]
        
        left+=1
        right-=1
    print(L)
3、插入排序

分为排好序区和未排序区，每次取未排序首位temp，从排序区尾部比较着往前走，只要temp小，未排序区刚比较过的就往后走一位，否则temp直接占位踩死

def insertsort(L):
    l = len(L)
    for i in range(1,l):
        j = i
        temp = L[i]
        while temp<L[j-1] and j>0:
            L[j] = L[j-1]
            j = j-1
        L[j] = temp
        print(L)
    print(L)
如果把temp 的地方都换成L[i]结果就不对了，不知道为什么

4、希尔排序

希尔排序是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，即插入排序。

def shellsort(L):
    l = len(L)
    gap = l//2
    while gap>0:
        for i in range(gap,l):
            temp = L[i]
            j = i
            while j>=gap and L[j-gap]>temp:
                L[j] = L[j-gap]
                j = j - gap
            L[j] = temp
        gap = gap//2
    print(L)
5、归并排序

def mergesort(L):
    l = len(L)
    if l<=1:
        return L
    mid = l//2
    left = mergesort(L[:mid])
    right = mergesort(L[mid:])
    return merge2(left,right)
def merge2(a,b):
    c = []
    l = 0
    r = 0
    while l<len(a) and r<len(b):
        if a[l]<b[r]:
            c.append(a[l])
            l+=1
        else:
            c.append(b[r])
            r+=1
    if l<=len(a):
        c = c+a[l:]
    if r<=len(b):
        c = c+b[r:]
    return c
    
L=[1,32,4,2,11,0,12,-2,333]
re = mergesort(L) 
奇怪的是mergesort（）里的return 写成print就报错，不知道为什么

原地归并



6、快速排序

找一个基准，这里用的是第一个数据，大于此数的放在右边，小于的放在左边，实作时，两个指针i和index，刚开走如果都小于基准，i和index都往后走，直到不小于，index记录这个第一个不小于的位置，i继续往后走找到第一个小于基准的数，将i和index所指的数据交换，i和index继续往后；最后的终止条件是i到达最后一个数据。

def quicksort(L,left=None,right=None):
    left = left if left else 0
    right = right if right else len(L)-1
    if left<right:
        indx = partition(L,left,right)
        quicksort(L,left,indx-1)
        quicksort(L,indx+1,right)
    return L
def partition(L,left,right):
    pre = left
    index = left+1
    i = left+1
    while i<=right:
        if L[i]<L[pre]:
            swap(L,i,index)
            index = index+1
        i = i+1
    swap(L,pre,index-1)
    return index-1
def swap(L,i,j):
    L[i],L[j] = L[j],L[i]
L=[1,32,4,2,11,0,12,-2,333]
quicksort(L)    
7、计数排序

这个排序方式用起来条件很高，虽然时间复杂度低；根据最大元素数据开辟桶的大小，每个桶对应一个数据；

装桶：遍历原数据的同时对应桶的计数加一

取数：遍历桶，每个桶代表的元素乘以此桶的计数

def countingsort(L):
    maxx = max(L)
    minn = min(L)
    l = maxx+1
    bu = [0]*l
    for i in L:
        bu[i] = bu[i] +1
    re = []
    for i in range(l):
        if bu[i]:
            re += [i]*bu[i]
    print(re)
L=[1,32,4,2,11,2,12,333]
countingsort(L)
8、桶排序

分桶：也就是分区，桶之间是有顺序的

遍历数据，将每个数据映射到对应的桶中

每个桶内数据各自排序

取数

def bucketSort(L):
    bucketsize = 10
    maxx = max(L)
    minn = min(L)
    #分桶
    bucketnum = (maxx-minn)//bucketsize+1    
    bucket = [[]]*bucketnum

    #数据隐射到桶中
    for i in L:
        index = (i-minn)//bucketsize
        bucket[index] = bucket[index] + [i]
    #每个桶内排序，随便什么方法了
    re = []
    for b in bucket:
        b.sort()
        if b:
            re = re + b
    print(re)
L=[1,32,4,2,11,2,12,333,200]
bucketSort(L)
9、基数排序

首先找出位数最多的数据的位数，一次按照个位、十位、百位....放到不同0~9的桶中，放一次取出来一次覆盖掉原来的数据，直到位数取完

def radix_sort(L):
    i = 0
    j = len(str(max(L)))
    while i<j:
        bucket = [[] for _ in range(10)]#十个桶0~9
        #桶中装数
        for t in L:
            bucket[(t//10**i)%10].append(t)
        #从桶中取数，覆盖掉原来的L
        L.clear()
        for k in bucket:
            L = L + k
        i = i+1
    print(L)
L=[1,32,4,2,11,2,12,333,200]
radix_sort(L)
10、堆排序

大根堆：父节点都比子节点大的二叉树

小根堆：父节点都比子节点小的二叉树

大根堆的向下调整，当根节点的左右子树都是堆，通过一次向下调整将其变成一个堆，一次比较根节点的孩子和根节点的大小，根大，停止，根小大的上，跟换到大的孩子位子上继续向下比较。

以大根堆为例降序排列，假设已经建好一个堆，取出根节点，用最后一个节点的代替根节点，向下调整，完成后取出根节点，依次。

建堆：从最后一个有孩子的节点逆序直到根节点，每次以此节点为根节点进行堆的向下调整

#向下调整
def sift(L,low,high):#L是树，low是树根，high是树的最后一个位置
    temp = L[low]
    i = low #指向根节点
    j = 2*i + 1 #指向孩子节点
    while j<=high:
        if j+1<=high and L[j+1]>L[j]:
            j = j+1 #j指向大孩子节点
        #比较j和temp，temp大结束调整，否则换位
        if L[j]>temp:
            L[i] = L[j]
            i = j
            j = 2*i +1
        else:
            break
    L[i] = temp
    
def heap_sort(L):
    n = len(L)
#建立堆
    for low in range(n//2-1,-1,-1):
        sift(L,low,n-1)
#出数
    for high in range(n-1,-1,-1):
        L[0],L[high] = L[high],L[0]
        sift(L,0,high-1)        
        
L=[1,32,4,2,11,2,12,333,200]
heap_sort(L)
print(L)    