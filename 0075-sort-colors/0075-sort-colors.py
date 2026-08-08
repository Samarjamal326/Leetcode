class Solution:

    def sortColors(self, a: List[int]) -> None:
        
        high = len(a) - 1
        low = 0
        mid = 0

        while mid <= high:
            if a[mid] == 0:
                a[mid], a[low] = a[low], a[mid]
                mid += 1
                low += 1
        
            elif a[mid] == 1:
                mid += 1
        
            else:
                a[mid], a[high] = a[high], a[mid]
                high -= 1
    