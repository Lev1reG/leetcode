class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0
        tPtr = 0

        if len(s) == 0:
            return True

        while tPtr < len(t) and sPtr < len(s):
            if s[sPtr] == t[tPtr]:
                sPtr += 1
                tPtr += 1
                continue
            else:
                tPtr += 1
        
        if sPtr != len(s):
            return False
        else:
            return True