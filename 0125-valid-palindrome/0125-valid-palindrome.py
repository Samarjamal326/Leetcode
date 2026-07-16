class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        s = s.lower()
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")
        print(s)

        l = 0
        r = len(s) - 1
        print(l)


        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True 