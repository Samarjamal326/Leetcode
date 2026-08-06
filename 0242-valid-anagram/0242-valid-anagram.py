from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqs = defaultdict(int)
        freqt = defaultdict(int)

        for i in s:
            freqs[i] += 1
        print(freqs)
        for j in t:
            freqt[j] += 1

        if freqs == freqt:
            return True
        else:
            return False