class Solution:
    def climbStairs(self, n: int) -> int:
        def _climb_stairs_helper(m: int) -> tuple[int, int]:  # (f(m), f(m - 1))
            if m == 1:
                return 1, 1

            one_step_before, two_steps_before = _climb_stairs_helper(m - 1)
            return one_step_before + two_steps_before, one_step_before

        return _climb_stairs_helper(n)[0]
