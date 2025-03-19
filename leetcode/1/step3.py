from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            if (complement_i := index_map.get(target - num)) is not None:
                return [i, complement_i]
            else:
                index_map[num] = i

        raise ValueError("No valid solution found")
