class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for idx in range(1, len(prices)):
            if prices[idx - 1] < prices[idx]:
                maxProfit += prices[idx] - prices[idx - 1]
        
        return maxProfit