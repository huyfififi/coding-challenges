class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_index = len(a) - 1
        b_index = len(b) - 1

        answer: list[str] = []
        carry = 0
        while a_index >= 0 or b_index >= 0 or carry == 1:
            total = 0
            if a_index >= 0:
                total += int(a[a_index])
            if b_index >= 0:
                total += int(b[b_index])
            total += carry

            answer.append(str(total % 2))
            carry = total // 2

            a_index -= 1
            b_index -= 1

        return "".join(reversed(answer))
