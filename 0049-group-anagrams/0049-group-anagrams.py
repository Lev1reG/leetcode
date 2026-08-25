class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for word in strs:
            sorted_str = "".join(sorted(word))
            anagram_group[sorted_str].append(word)
        
        return list(anagram_group.values())