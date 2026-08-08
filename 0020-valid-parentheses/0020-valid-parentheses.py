class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        if len(s)%2 != 0:
            return False

        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                opened.append(s[i])
            elif len(opened) == 0:
                return False
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(opened) == 0:
                    return False

                if opened[-1] != pairs[s[i]]:
                    return False

                opened.pop()
                
        if len(opened) == 0:
            return True
        else:
            return False