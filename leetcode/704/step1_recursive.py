class Solution(object):
    def search(self, nums, target):
        return self._binary_search(nums, target, 0, len(nums) - 1)

    def _binary_search(self, nums, target, start_i, end_i):
        if start_i > end_i:
            return -1

        middle_i = (start_i + end_i) // 2
        if nums[middle_i] == target:
            return middle_i
        if nums[middle_i] < target:
            return self._binary_search(nums, target, middle_i + 1, end_i)
        return self._binary_search(nums, target, start_i, middle_i - 1)
