class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x // 2
        ans = 1

        if x < 2:
            return x

        while low <= high:
            mid = low + ((high - low) // 2)
            pow_mid = mid * mid
            if pow_mid == x:
                return mid
            elif pow_mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans