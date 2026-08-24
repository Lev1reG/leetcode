class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        minLen = inf
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                minLen = min((right - left + 1), minLen)
                sum -= nums[left]
                left += 1
        
        if minLen == inf:
            return 0
        
        return minLen
            