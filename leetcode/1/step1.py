from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: O(n), Space complexity: O(n)
        nums_sorted: tuple[int, int] = sorted(
            [(n, i) for i, n in enumerate(nums)],
            key=lambda x: x[0],
        )

        li = 0
        ri = len(nums) - 1
        while li < ri:
            _sum = nums_sorted[li][0] + nums_sorted[ri][0]
            if _sum == target:
                return [
                    nums_sorted[li][1],
                    nums_sorted[ri][1],
                ]
            elif _sum < target:
                li += 1
            else:
                ri -= 1

        return [-1, -1]  # This should not happen
