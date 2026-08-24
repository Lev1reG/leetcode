class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestLen = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                x = num + 1

                while x in numsSet:
                    x += 1

                longestLen = max((x - num), longestLen)

        return longestLen

