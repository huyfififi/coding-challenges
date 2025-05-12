class Solution:
    def climbStairs(self, n: int) -> int:
        def _climb_stairs_helper(m: int) -> tuple[int, int]:  # (f(m - 1), f(m))
            if m == 1:
                return 1, 1
            if m == 2:
                return 1, 2

            prev_2, prev_1 = _climb_stairs_helper(m - 1)
            return prev_1, prev_1 + prev_2

        return _climb_stairs_helper(n)[1]
