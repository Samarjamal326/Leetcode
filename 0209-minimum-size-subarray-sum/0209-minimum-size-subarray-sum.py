class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sums = 0
        l = 0
        min_sum = float("inf")

        for r in range(len(nums)):
            sums += nums[r]

            while sums >= target:
                min_sum = min(min_sum, r - l + 1)

                sums -= nums[l]
                l += 1

        if min_sum == float("inf"):
            return 0

        return min_sum