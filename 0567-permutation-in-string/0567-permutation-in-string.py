class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        freq = {}
        window = {}

        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        for r in range(len(s2)):

            window[s2[r]] = window.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            if r - l + 1 == len(s1):
                if window == freq:
                    return True

        return False