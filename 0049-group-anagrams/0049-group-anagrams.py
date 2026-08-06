from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]

        n = len(strs)
        
        freq = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            freq[key].append(word)

        return list(freq.values())