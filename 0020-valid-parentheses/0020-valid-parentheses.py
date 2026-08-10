class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        opened = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                opened.append(s[i])

            elif len(opened) == 0:
                return False

            elif opened[-1] == pairs[s[i]]:
                opened.pop()

            else:
                return False

        return len(opened) == 0