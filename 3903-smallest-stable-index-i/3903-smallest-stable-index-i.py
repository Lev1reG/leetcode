class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            idx = i + 1
            instability = max(nums[:idx]) - min(nums[i:])
            if instability <= k:
                return i
        
        return -1