class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefixLen = len(prefix)

        for str in strs:
            while prefix != str[:prefixLen]:
                prefixLen -= 1

                if prefixLen == 0:
                    return ""
                
                prefix = prefix[:prefixLen]
        
        return prefix