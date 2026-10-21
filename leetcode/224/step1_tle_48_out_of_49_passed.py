import string


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        cursor = 0
        result = 0
        positive = True
        while cursor < len(s):
            if s[cursor] == " ":
                cursor += 1
                continue
            if s[cursor] == "+":
                positive = True
                cursor += 1
                continue
            if s[cursor] == "-":
                positive = False
                cursor += 1
                continue

            if s[cursor] == "(":
                right = cursor + 1
                num_open = 1
                while 0 < num_open:
                    if s[right] == "(":
                        num_open += 1
                    elif s[right] == ")":
                        num_open -= 1

                    right += 1

                # sub_result = self.calculate(s[cursor + 1 : right])
                sub_result = self.calculate(s[cursor + 1 : right - 1])
                result += sub_result if positive else -sub_result
                # cursor = right + 1
                cursor = right
                continue

            chunk_num = 0
            while cursor < len(s) and s[cursor] in string.digits:
                chunk_num *= 10
                chunk_num += int(s[cursor])
                cursor += 1
            result += chunk_num if positive else -chunk_num

        return result
