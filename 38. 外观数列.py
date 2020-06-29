
这个题目好难读
1
2 描述的是1，是一个1，也就是11
3 描述的是11，是两个1，也就是21
4 描述的是21，是一个2一个1，也就是12-11
5 描述的是1211, 是一个1，一个2，两个1，也就是11-12-21
6 描述的是111221，是三个1，两个2，一个1，也就是31-22-11
7 描述的是312211，是一个3一个1两个2两个1，也即是13-11-22-21   找连续个数+描述的连续的数本体
以此类推

class Solution:
    def countAndSay(self, n: int) -> str:
        if n<0:
            return ''
        if n==1:
            return '1'
        seq = self.countAndSay(n-1)
        next_seq = ''
        cnt = 1
        for i in range(len(seq)):
            if i+1<len(seq) and seq[i]==seq[i+1]:
                cnt+=1
            else:
                next_seq = next_seq + str(cnt)
                next_seq = next_seq + seq[i]
                cnt = 1
        return next_seq