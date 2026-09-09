class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0
        end = 0
        
        if len(nums) == 0:
            return result

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                if start == end:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start]) + "->" + str(nums[end]))
                start = i
                end = i
            else:
                end += 1
        
        if start == end:
            result.append(str(nums[start]))
        else:
            result.append(str(nums[start]) + "->" + str(nums[end]))

        return result