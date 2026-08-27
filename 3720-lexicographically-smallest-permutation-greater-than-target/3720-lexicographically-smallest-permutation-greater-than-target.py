class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(target)
        
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        match_len = 0
        while match_len < n:
            c_idx = ord(target[match_len]) - ord('a')
            if count[c_idx] == 0:
                break
            count[c_idx] -= 1
            match_len += 1
        
        if match_len == n:
            match_len -= 1
            count[ord(target[match_len]) - ord('a')] += 1

        for idx in range(min(match_len, n - 1), -1, -1):
            target_val = ord(target[idx]) - ord('a')
            greater_char = None
            for i in range(target_val + 1, 26):
                if count[i] > 0:
                    greater_char = (chr(ord('a') + i))
                    count[i] -= 1
                    break

            if greater_char is not None:
                tail = []
                for i in range(26):
                    if count[i] > 0:
                        tail.append(chr(ord('a') + i) * count[i])
                
                return target[:idx] + greater_char + "".join(tail)
            
            if idx > 0:
                count[ord(target[idx - 1]) - ord('a')] += 1
            
        return ""