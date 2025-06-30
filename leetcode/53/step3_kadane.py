class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_ending_sum = 0
        max_sum = float("-inf")
        for num in nums:
            max_ending_sum = max(max_ending_sum + num, num)
            max_sum = max(max_sum, max_ending_sum)
        return max_sum
