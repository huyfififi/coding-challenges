class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        prev_2 = 1
        prev_1 = 1
        for i in range(2, n + 1):
            prev_2, prev_1 = prev_1, prev_1 + prev_2
        return prev_1
