class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []
        for c in s:
            if c in open_to_close:
                stack.append(c)
                continue

            if not stack:
                return False

            if open_to_close[stack.pop()] != c:
                return False

        return not stack
