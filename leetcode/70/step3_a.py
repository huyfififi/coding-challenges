class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_step_before = 2
        two_steps_before = 1
        for i in range(3, n + 1):
            one_step_before, two_steps_before = (
                one_step_before + two_steps_before,
                one_step_before,
            )
        return one_step_before
