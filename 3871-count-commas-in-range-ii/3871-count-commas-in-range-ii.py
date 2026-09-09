class Solution:
    def countCommas(self, n: int) -> int:
        if n // 1000 == 0:
            return 0
        
        count = 0
        k = 3

        while n >= 10**k:
            count += n - 10**k + 1
            k += 3
        
        return count