class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        while low < high:
            hours = 0
            mid = (low + high) // 2

            for i in piles:
                hours += ceil(i / mid)
            if hours > h:
                low = mid + 1
            else:
                high = mid
        
        return low