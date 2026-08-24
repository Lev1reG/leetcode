class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we'll use hash map of key is the num & value is the number repeated
        # iterate through nums 1 until m, dictonary[num1] ++
        # iterate thorough nums 2, dictonary[num2] ++
        # access all of the dictionary, update the nums
        counts = {}
        for num1 in nums1[:m]:
            counts[num1] = counts.get(num1, 0) + 1
        for num2 in nums2:
            counts[num2] = counts.get(num2, 0) + 1

        idx = 0
        for key, value in sorted(counts.items()):
            for _ in range(value):
                nums1[idx] = key
                idx += 1