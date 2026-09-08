class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                nums[idx] = nums[i]
                idx += 1
        
        return idx