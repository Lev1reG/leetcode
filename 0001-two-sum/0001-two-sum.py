class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for idx, num in enumerate(nums):
            pair_needed = target - num
            if pair_needed in pair_idx:
                return [idx, pair_idx[pair_needed]]
            else:
                pair_idx[num] = idx
        
        return []