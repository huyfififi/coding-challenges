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

            result += chunk * sign
            chunk = 0

            if c in "+-":
                sign = 1 if c == "+" else -1
                continue

            if c == "(":
                results_and_signs.append((result, sign))
                result = 0
                sign = 1
                continue
            if c == ")":
                last_result, last_sign = results_and_signs.pop()
                result = last_result + result * last_sign

        return result + chunk * sign
