import enum
import string


class Sign(enum.Enum):
    POSITIVE = "+"
    NEGATIVE = "-"


class Solution:
    def calculate(self, s: str) -> int:
        results = []
        signs = []

        result = 0
        sign = Sign.POSITIVE
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue

            if s[i] == "(":
                results.append(result)
                signs.append(sign)
                sign = Sign.POSITIVE
                result = 0
                i += 1
                continue
            if s[i] == ")":
                sign = signs.pop()
                if sign == Sign.NEGATIVE:
                    result = -result

                result += results.pop()
                i += 1
                continue

            if s[i] == Sign.POSITIVE.value:
                sign = Sign.POSITIVE
                i += 1
                continue
            if s[i] == Sign.NEGATIVE.value:
                sign = Sign.NEGATIVE
                i += 1
                continue

            chunk = 0
            while i < len(s) and s[i] in string.digits:
                chunk = chunk * 10 + int(s[i])
                i += 1
            result += chunk if sign == Sign.POSITIVE else -chunk

        return result
