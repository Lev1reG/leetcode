class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}

        for c in magazine:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        
        for m in ransomNote:
            if m in map and map[m] > 0:
                map[m] -= 1
                continue
            else:
                return False
        
        return True