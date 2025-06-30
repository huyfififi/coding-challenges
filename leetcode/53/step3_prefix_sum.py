class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_subarray_sum = float("-inf")
        for num in nums:
            prefix_sum += num
            max_subarray_sum = max(max_subarray_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return max_subarray_sum
