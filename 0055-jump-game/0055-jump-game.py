class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = 0

        for i in range(len(nums) - 1):
            maxStep = max(maxStep, nums[i])
            maxStep -= 1
            if maxStep < 0:
                return False
        
        return True