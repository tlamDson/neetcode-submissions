from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for l in strs:
            key = ''.join(sorted(l))
            anagrams[key].append(l)  
        result = list(anagrams.values())
        return result