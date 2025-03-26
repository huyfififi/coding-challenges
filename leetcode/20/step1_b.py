class Solution:
    def isValid(self, s: str) -> bool:
        PARENTHESE_PAIRS = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        l = []  # used as a stack
        for c in s:
            if l and PARENTHESE_PAIRS.get(l[-1]) == c:
                l.pop()
            else:
                l.append(c)

        return l == []
