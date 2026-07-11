class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False

        freqs = {}
        freqt = {}

        for i in s:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1

        for j in t:
            if j in freqt:
                freqt[j] += 1
            else:
                freqt[j] = 1

        return freqs == freqt