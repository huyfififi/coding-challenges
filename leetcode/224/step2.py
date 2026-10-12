class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        chunk = 0
        sign = 1
        results_and_signs = []

        for c in s:
            if c == " ":
                continue

            if c.isdigit():
                chunk = chunk * 10 + int(c)
                continue

            if c in "+-":
                result += chunk * sign
                sign = 1 if c == "+" else -1
                chunk = 0
                continue

            if c == "(":
                results_and_signs.append((result, sign))
                result = 0
                sign = 1
                continue

            if c == ")":
                result += chunk * sign
                last_result, last_sign = results_and_signs.pop()
                result = last_result + result * last_sign
                chunk = 0

        return result + chunk * sign
