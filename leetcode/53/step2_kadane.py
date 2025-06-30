class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_ending = 0
        max_sum = float("-inf")
        for num in nums:
            max_ending = max(max_ending + num, num)
            max_sum = max(max_sum, max_ending)
        return max_sum
