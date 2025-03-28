class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i : i + 2] in ("()", "{}", "[]"):
                return self.isValid(s[:i] + s[i + 2 :])

        return s == ""
