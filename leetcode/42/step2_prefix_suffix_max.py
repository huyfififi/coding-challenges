import collections


class Solution:
    def trap(self, height: list[int]) -> int:
        prefix_max = [height[0]]
        for i in range(1, len(height)):
            prefix_max.append(max(prefix_max[-1], height[i]))

        suffix_max = collections.deque([height[-1]])
        for i in range(len(height) - 2, -1, -1):
            suffix_max.appendleft(max(suffix_max[0], height[i]))

        filling = 0
        for i in range(len(height)):
            capped_height = min(prefix_max[i], suffix_max[i])
            filling = capped_height - height[i]

        return filling
