class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        count = 1
        longest = 0

        s = set(nums)
        print(s)

        if len(s) < 2:
            return 1

        sorted_s = sorted(s)
        print(sorted_s)

        for i in range(0,len(sorted_s)-1):
            if sorted_s[i] == sorted_s[i+1] - 1:
                count += 1
                print(longest)
            else:
                count = 1
                print(count)
            longest = max(longest, count)
        
        return longest