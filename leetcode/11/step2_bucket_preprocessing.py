import collections


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_height = max(height)
        height_to_rightmost = [-1] * (max_height + 1)
        height_to_leftmost = [float("inf")] * (max_height + 1)
        for i, h in enumerate(height):
            height_to_rightmost[h] = max(height_to_rightmost[h], i)
            height_to_leftmost[h] = min(height_to_leftmost[h], i)
        assert len(height_to_rightmost) == len(height_to_leftmost)

        min_height_to_rightmost = height_to_rightmost.copy()
        min_height_to_leftmost = height_to_leftmost.copy()
        for h in range(max_height - 1, -1, -1):
            min_height_to_rightmost[h] = max(
                min_height_to_rightmost[h], min_height_to_rightmost[h + 1]
            )
            min_height_to_leftmost[h] = min(
                min_height_to_leftmost[h], min_height_to_leftmost[h + 1]
            )

        max_area = 0
        for i, h in enumerate(height):
            right = min_height_to_rightmost[h]
            left = min_height_to_leftmost[h]
            max_area = max(
                max_area,
                (right - i) * h,
                (i - left) * h,
            )

        return max_area
