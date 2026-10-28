class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        left_next_min = [-1] * n
        right_next_min = [n] * n
        left_shorter = []
        right_shorter = []
        max_area = 0
        for i in range(n):
            while left_shorter and heights[i] <= heights[left_shorter[-1]]:
                left_shorter.pop()
            if left_shorter:
                left_next_min[i] = left_shorter[-1]
            left_shorter.append(i)

        for i in range(n - 1, -1, -1):
            while right_shorter and heights[i] <= heights[right_shorter[-1]]:
                right_shorter.pop()
            if right_shorter:
                right_next_min[i] = right_shorter[-1]
            right_shorter.append(i)

        for i in range(n):
            max_area = max(
                max_area, heights[i] * (right_next_min[i] - left_next_min[i] - 1)
            )

        return max_area
