from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer: list[str] = []
        carry = 0
        for bit_a, bit_b in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            total = int(bit_a) + int(bit_b) + carry
            answer.append(str(total % 2))
            carry = total // 2

        if carry == 1:
            answer.append("1")

        return "".join(reversed(answer))
