from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        s1 = ""
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        sorted_items = sorted(freq.items(), key= lambda x :x[1], reverse=True)

        for i in range(len(sorted_items)):
            char = sorted_items[i][0]
            count = sorted_items[i][1]

            s1 += char * count            
        return s1