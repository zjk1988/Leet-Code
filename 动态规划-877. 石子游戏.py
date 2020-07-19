class pair(object):
    def __init__(self,first,sec):
        self.first = first
        self.sec = sec
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[] for i in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i].append(pair(0,0))
        for i in range(l):
            dp[i][i].first = piles[i]
            dp[i][j].sec = 0
        for i in range(l-1,-1,-1):
            for j in range(i+1,l):
                left = piles[i] + dp[i+1][j].sec
                right = piles[j] + dp[i][j-1].sec
                if left>right:
                    dp[i][j].first = left
                    dp[i][j].sec =  dp[i+1][j].first
                else:
                    dp[i][j].first = right
                    dp[i][j].sec = dp[i][j-1].first
        return dp[0][l-1].first-dp[0][l-1].sec
