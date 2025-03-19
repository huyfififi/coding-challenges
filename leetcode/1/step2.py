from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity: O(n), Space complexity: O(n)

        index_map = {}  # {num, index}
        
        for i, num in enumerate(nums):
            if target - num in index_map:
                return [i, index_map[target - num]]
            else:
                index_map[num] = i
        
        return [-1, -1]  # This should not happen
