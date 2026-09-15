class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        end = -1

        for i in range(n):
            for j in (i - 1, i):
                l, r = j, i

                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 >= k and l > end:
                        count += 1
                        end = r
                        break
                    
                    l -= 1
                    r += 1
        
        return count