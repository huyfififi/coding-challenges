class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.rjust(len(b), "0")
        b = b.rjust(len(a), "0")

        answer: list[str] = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            answer.append(str(total % 2))
            carry = total // 2

        if carry == 1:
            answer.append("1")

        return "".join(reversed(answer))
