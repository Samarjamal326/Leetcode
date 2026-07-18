class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        count = 0
        max_count = 0

        seen = set()

        if len(s) == 0:
            return 0
        if len(s) < 2:
            return 1

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_count = max(max_count, r - l + 1)
            
        return max_count