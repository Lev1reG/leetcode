class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[idx] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                if sum < 0:
                    left += 1
                if sum == 0:
                    result.append([nums[idx], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result