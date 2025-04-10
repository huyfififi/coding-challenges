class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_i, right_i = 0, len(s) - 1

        while left_i < right_i:
            if not s[left_i].isalnum():
                left_i += 1
                continue

            if not s[right_i].isalnum():
                right_i -= 1
                continue

            if s[left_i].lower() != s[right_i].lower():
                return False

            left_i += 1
            right_i -= 1

        return True
