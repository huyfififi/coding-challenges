from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement_i = num_to_index.get(target - num)
            if complement_i is not None:
                return [i, complement_i]

            num_to_index[num] = i

        return []
