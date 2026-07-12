class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        s = set(nums)
        longest = 0

        for nums in s:

            if nums - 1 not in s:
                current = nums
                lenght =  1

                while current + 1 in s:
                    current += 1
                    lenght += 1

                longest = max(longest, lenght)
        
        return longest