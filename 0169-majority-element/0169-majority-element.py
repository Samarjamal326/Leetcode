from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return sorted_freq[0][0]