class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if m != n:
            return False

        freq = {}
        freqs = {}

        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for j in t:
            if j in freqs:
                freqs[j] += 1
            else:
                freqs[j] = 1
        
        return freq == freqs