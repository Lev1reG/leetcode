class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = []

        for idx in range(len(nums)):
            if idx == 0:
                subseq.append(nums[idx])
                continue
            else:
                if subseq[len(subseq) - 1] < nums[idx]:
                    subseq.append(nums[idx])
                else:
                    left = 0
                    right = len(subseq) - 1
                    while left <= right:
                        mid = (left + right) // 2
                        if left == right == mid:
                            subseq[mid] = nums[idx]
                            break
                        elif subseq[mid] >= nums[idx]:
                                right = mid
                        else:
                                left = mid + 1
        
        return len(subseq)
