from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Padding
        a = "0" * (len(b) - len(a)) + a
        b = "0" * (len(a) - len(b)) + b

        answer = deque()
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            digit = int(a[i]) + int(b[i]) + carry
            answer.appendleft(str(digit % 2))
            carry = digit // 2

        if carry == 1:
            answer.appendleft("1")
        return "".join(answer)
