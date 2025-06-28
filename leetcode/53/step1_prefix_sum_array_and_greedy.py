class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefix_sum_array = [0]
        for num in nums:
            prefix_sum_array.append(prefix_sum_array[-1] + num)

        max_subarray_sum = max(nums)
        min_prefix_sum_so_far = float("inf")
        for prefix_sum in prefix_sum_array:
            if prefix_sum < min_prefix_sum_so_far:
                min_prefix_sum_so_far = prefix_sum
                continue
            max_subarray_sum = max(max_subarray_sum, prefix_sum - min_prefix_sum_so_far)

        return max_subarray_sum
