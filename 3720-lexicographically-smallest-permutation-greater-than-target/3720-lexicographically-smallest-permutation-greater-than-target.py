class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(target)
        
        for idx in range(n - 1, -1, -1):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            can_form_prefix = True
            for c in target[:idx]:
                if count[ord(c) - ord('a')] == 0:
                    can_form_prefix = False
                count[ord(c) - ord('a')] -= 1
            
            if not can_form_prefix:
                continue

            greater_char = None
            for i in range(ord(target[idx]) + 1, ord('z') + 1):
                i -= ord('a')
                if count[i] > 0:
                    greater_char = (chr(ord('a') + i))
                    count[i] -= 1
                    break

            if greater_char is None:
                continue

            tail = []
            for i in range(26):
                if count[i] > 0:
                    tail.append(chr(ord('a') + i) * count[i])
            
            return target[:idx] + greater_char + "".join(tail)
            
        return ""