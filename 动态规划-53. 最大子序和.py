class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l==0:
            return 0
        dp = nums
        for i in range(1,l):
            dp[i] = max(dp[i-1]+nums[i],dp[i])
        return max(dp)