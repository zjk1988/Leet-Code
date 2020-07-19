class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob1(nums[1:]),self.rob1(nums[:-1]))
    def rob1(self, nums):
        l = len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[-1]
        if l==2:
            return max(nums)
        dp = [0]*(l+2)
        for i in range(l):
            dp[i+2] = max(dp[i+1],dp[i]+nums[i])
        return dp[-1]