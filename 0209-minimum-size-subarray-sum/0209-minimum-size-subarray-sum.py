class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sums= 0
        r = 0
        l = 0
        min_sum = float('inf')

        while r < len(nums):

            sums += nums[r]
                
            while sums >= target:
                min_sum = min(r - l + 1, min_sum)
                sums -= nums[l]

                l+=1
            r += 1

        if min_sum == float('inf'):
            return 0
        
        return min_sum