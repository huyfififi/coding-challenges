import functools


class Solution:
    def maxArea(self, height: list[int]) -> int:
        @functools.cache
        def max_area_helper(first: int, last: int) -> int:
            if last <= first:
                return 0

            return max(
                (last - first) * min(height[first], height[last]),
                max_area_helper(first + 1, last),
                max_area_helper(first, last - 1),
            )

        return max_area_helper(0, len(height) - 1)
