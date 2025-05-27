from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_to_count = Counter(nums)

        for num, count in num_to_count.items():
            if count > len(nums) // 2:
                return num

        raise ValueError("No majority element found in the given numbers.")
