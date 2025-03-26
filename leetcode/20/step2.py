class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []  # stack to store opening brackets
        for c in s:
            if c in bracket_pairs:
                stack.append(c)
                continue

            if not stack:
                return False

            if bracket_pairs[stack.pop()] != c:
                return False

        return not stack
