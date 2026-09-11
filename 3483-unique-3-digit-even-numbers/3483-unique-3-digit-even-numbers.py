class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        count = 0

        for digit in digits:
            freq[digit] += 1
         
        for i in range(100, 1000, 2):
            d1 = i // 100
            d2 = (i // 10) % 10
            d3 = i % 10

            freq[d1] -= 1
            freq[d2] -= 1
            freq[d3] -= 1

            if freq[d1] >= 0 and freq[d2] >= 0 and freq[d3] >= 0:
                count += 1
            
            freq[d1] += 1
            freq[d2] += 1
            freq[d3] += 1

        return count