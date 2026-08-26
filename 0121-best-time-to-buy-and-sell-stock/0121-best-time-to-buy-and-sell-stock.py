class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        balance = -prices[0]
        profit = 0
        for price in prices[1:]:
            balance = max(balance, -price)
            profit = max(profit, balance + price)

        return profit