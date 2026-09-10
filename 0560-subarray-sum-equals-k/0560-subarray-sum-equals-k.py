class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        freq = {0:1}
        needed = 0
        count = 0

        for i in range(len(nums)):
            prefix += nums[i]

            needed = prefix - k
            if needed in freq:
                count += freq[needed]
            
            freq[prefix] = freq.get(prefix, 0) + 1

        return count