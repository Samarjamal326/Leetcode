class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        freq = {}
        ans = 0
        replacements = 0
        
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            window_size = r - l + 1
            max_freq = max(freq.values())
            replacements = window_size - max_freq

            while replacements > k:
                if s[l] in freq:
                    freq[s[l]] -= 1
                l += 1

                window_size = r - l + 1
                max_freq = max(freq.values())
                replacements = window_size - max_freq
            ans = max(ans, r - l + 1)
        
        return ans