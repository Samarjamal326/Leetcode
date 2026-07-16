class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        volume = 0
        length = 0
        max_volume = 0

        while l < r:
            heights = min(height[l], height[r])
            length = r - l

            volume = heights * length
            max_volume = max(max_volume, volume)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_volume