import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        if s == " ":
            return True
        
        s = s.lower()
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")  

        if s == s[::-1]:
            return True
        else:
            return False