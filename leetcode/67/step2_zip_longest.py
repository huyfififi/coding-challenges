from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer: list[str] = []
        carry = 0
        for digit_a, digit_b in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            total = int(digit_a) + int(digit_b) + carry
            answer.append(str(total % 2))
            carry = total // 2

        if carry == 1:
            answer.append("1")
        return "".join(reversed(answer))
