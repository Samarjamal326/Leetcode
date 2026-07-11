class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,nums in enumerate(nums):
            needed = target - nums

            if needed in seen:
                return [seen[needed], i]
            
            seen[nums] = i