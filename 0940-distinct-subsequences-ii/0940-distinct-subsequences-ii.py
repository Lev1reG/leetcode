class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends = [0] * 26
        running_sum = 0

        for ch in s:
            idx = ord(ch) - ord('a')

            new_ends = (running_sum + 1) % MOD

            running_sum = (running_sum + new_ends - ends[idx]) % MOD
            ends[idx] = new_ends
        
        return running_sum