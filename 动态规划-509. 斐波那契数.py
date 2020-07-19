class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        f_1,f_2 = 0,1
        for i in range(N-1):
            f_1,f_2 = f_2,f_1+f_2
        return f_2