from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_to_count = defaultdict(int)
        for num in nums:
            num_to_count[num] += 1
            if num_to_count[num] > len(nums) // 2:
                return num

        raise ValueError("No majority element found.")
