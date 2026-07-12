from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        lists = []
        s = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_items = sorted(freq.items(), key = lambda x: x[1], reverse= True)

        for i in range(0, k):
            lists.append(sorted_items[i][0])

        return lists 