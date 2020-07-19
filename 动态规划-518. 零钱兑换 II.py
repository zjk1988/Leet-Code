class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        l = len(coins)
        # if l == 0:
        #     return 0
        import numpy as np
        dp = np.zeros(amount+1)
        dp[0] = 1
        for i in range(1,l+1):
            for j in range(1,amount+1):
                if j-coins[i-1]>=0:
                    dp[j] = dp[j] + dp[j-coins[i-1]]
                else:
                    dp[j] = dp[j]
        return int(dp[amount])