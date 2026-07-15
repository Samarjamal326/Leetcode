from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        ans = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        print(freq)
        sorted_items = sorted(freq.items(), key= lambda x : x[1], reverse = True)

        print(sorted_items)

        for i in range(0, k):
            ans.append(sorted_items[i][0])

        return ans