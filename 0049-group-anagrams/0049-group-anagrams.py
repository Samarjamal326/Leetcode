class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]

        freq = {}

        for words in strs:
            key = "".join(sorted(words))
            if key not in freq:
                freq[key] = [words]
            else:
                freq[key].append(words)
        
        return list(freq.values())