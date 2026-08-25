class Solution:
    def rob(self, nums: List[int]) -> int:
        # robber has 2 options -> rob house i or not rob
        # if rob house i, cannot rob i - 1 but safe to rob i - 2
        # if not rob, can rob i - 1
        # we need to find which one is more profitable
        # a) rob current house + loot house previous
        # b) rob previous house & its previous
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # dp[a] is the max loot can be collect until house a
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for house in range(2, len(nums)):
            dp[house] = max(dp[house - 1], dp[house - 2] + nums[house])
        
        return dp[-1]