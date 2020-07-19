class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l==0:
            return 0
        dp = [1]*l
        for i in range(l):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)