from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: O(n), Space complexity: O(n)

        index_map = {}  # {num, index}

        for i, num in enumerate(nums):
            if (complement_i := index_map.get(target - num)) is not None:
                return [i, complement_i]
            else:
                index_map[num] = i

        return [-1, -1]  # This should not happen
