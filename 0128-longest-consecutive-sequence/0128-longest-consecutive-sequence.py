class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = []
        sets = set(nums)
        s = sorted(sets)
        max_count, count = 0, 0
        i = 0

        if len(s) < 1:
            return 0

        for i in range(len(s)-1):
            if s[i+1] - s[i] == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
                i = i + 1
        
        return max_count + 1