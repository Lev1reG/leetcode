class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i, val in enumerate(nums):
            if val in map:
                if (i - map[val]) <= k:
                    return True
            map[val] = i
        
        return False
