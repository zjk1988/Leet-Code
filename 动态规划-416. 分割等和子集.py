# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s = sum(nums)
#         if s%2!=0:
#             return False
#         l = len(nums)
#         s = s//2
#         import numpy as np
#         dp = np.zeros(s+1)
#         dp[0] = 1
#         for i in range(1,l):
#             for j in range(s,-1,-1):
#                 if j>=nums[i]:
#                     dp[j] = dp[j] or dp[j-nums[i]]
#         return dp[s]



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return 0
        l = len(nums)
        s = s//2
        import numpy as np
        dp = np.zeros((l+1,s+1))
        for i in range(l+1):
            dp[i][0] = 1
        for i in range(1,l+1):
            for j in range(1,s+1):
                if j-nums[i-1]>=0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[l][s]