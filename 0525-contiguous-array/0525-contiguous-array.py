class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix = 0
        first = {0: -1}
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        for i in range(len(nums)):
            prefix += nums[i]

            if prefix in first:
                max_len = max(max_len, i - first[prefix])
            else:
                first[prefix] = i
        
        return max_len
        