class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        i = sorted(s)
        j = sorted(t)

        if i == j:
            return True
        else:
            return False