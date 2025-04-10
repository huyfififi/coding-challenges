class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars_to_validate: list[str] = []

        for c in s:
            if not c.isalnum():
                continue
            chars_to_validate.append(c.lower())

        return chars_to_validate == chars_to_validate[::-1]
