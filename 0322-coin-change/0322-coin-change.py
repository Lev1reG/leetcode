class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for target in range(1, amount + 1):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], dp[target - coin] + 1)
        
        if dp[amount] != inf:
            return dp[amount]
        else:
            return -1