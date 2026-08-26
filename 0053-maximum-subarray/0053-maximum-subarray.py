class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] max sum of sub array ending on i
        dp = [-inf] * len(nums)
        dp[0] = nums[0]

        # we need to decide to extend the sub array or start new
        for idx in range(1, len(nums)):
            dp[idx] = max(dp[idx - 1] + nums[idx], nums[idx])
        
        return max(dp)