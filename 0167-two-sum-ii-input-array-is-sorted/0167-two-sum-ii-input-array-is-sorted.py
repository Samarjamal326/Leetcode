class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        r = len(nums) - 1
        l = 0

        while l < r:
            sums = nums[l] + nums[r]
            if sums > target: r -= 1
            if sums < target: l += 1
            elif sums == target:
                return [l+1 , r+1]