class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        results = []

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                results.append(left + 1)
                results.append(right + 1)
            if sum > target:
                right -= 1
            else:
                left += 1
        
        return results