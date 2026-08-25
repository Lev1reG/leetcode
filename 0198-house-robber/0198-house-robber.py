class Solution:
    def rob(self, nums: List[int]) -> int:
        # robber has 2 options -> rob house i or not rob
        # if rob house i, cannot rob i - 1 but safe to rob i - 2
        # if not rob, can rob i - 1
        # we need to find which one is more profitable
        # a) rob current house + loot house previous
        # b) rob previous house & its previous
        def loot(nums: List[int], i) -> int:
            if (i < 0):
                return 0
            if (memo[i] >= 0):
                return memo[i]
            result = max(loot(nums, i - 2) + nums[i], loot(nums, i - 1))
            memo[i] = result
            return result

        memo = [-1]*len(nums)
        return loot(nums, len(nums) - 1)