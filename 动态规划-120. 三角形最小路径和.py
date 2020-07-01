class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle.copy()
        l = len(triangle)
        for i in range(1,l):
            dp[i][0] = dp[i-1][0] + dp[i][0]
        for i in range(1,l):
            for j in range(1,i+1):
                if i==j:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + dp[i][j]
        return min(dp[-1])
