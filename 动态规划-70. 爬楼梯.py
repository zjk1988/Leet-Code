class Solution:
    def climbStairs(self, n: int) -> int:
        a = []
        a.append(1)#第0个台阶
        a.append(1)#第1个台阶
        if n>=2:
            for i in range(2,n+1,1):
                a.append(a[-1]+a[-2])
        return a[-1]