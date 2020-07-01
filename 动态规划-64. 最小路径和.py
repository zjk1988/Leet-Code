class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lcol = len(grid[0])
        lrow = len(grid)
        dp = [[0 for i in range(lcol)] for j in range(lrow)]
        dp[0][0] = grid[0][0]
        i,j = 0,0
        for t in range(1,lrow):
            dp[t][0] = dp[t-1][0]+grid[t][0]            
        for t in range(1,lcol):
            dp[0][t] = dp[0][t-1]+grid[0][t]        
        for i in range(1,lrow):
            for j in range(1,lcol):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[lrow-1][lcol-1]