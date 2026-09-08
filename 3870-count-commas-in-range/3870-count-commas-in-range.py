class Solution:
    def countCommas(self, n: int) -> int:
        if n // 1000 == 0:
            return 0
        
        return n - 999