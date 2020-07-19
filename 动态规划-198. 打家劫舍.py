class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [-1]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
    
class Solution:
    def rob(self, nums: List[int]) -> int:
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
    

 class Solution:
     def rob(self, nums: List[int]) -> int:
         if len(nums)==0:
             return 0
         if len(nums)==1:
             return nums[0]
         # dp = [-1]*len(nums)
         # dp[0]=nums[0]
         dp_0 = nums[0]
         dp_1 = max(nums[0],nums[1])
         for i in range(2,len(nums)):
             dp_i = max(dp_1,dp_0+nums[i])
             dp_0 = dp_1
             dp_1 = dp_i
         return dp_1
