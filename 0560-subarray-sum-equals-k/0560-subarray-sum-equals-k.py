class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        freq = {0 : 1}
        ans = 0

        for num in nums:
            prefix += num
            needed = prefix - k
            if needed in freq:
                ans += freq[needed]

            freq[prefix] = freq.get(prefix, 0) + 1

        return ans