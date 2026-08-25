class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_seen = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in char_seen:
                char_seen.remove(s[left])
                left += 1
            char_seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen