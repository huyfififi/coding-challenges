class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def _binary_search(start_i: int, end_i: int) -> int:
            if start_i > end_i:
                return -1

            middle_i = (start_i + end_i) // 2
            if nums[middle_i] == target:
                return middle_i
            if nums[middle_i] < target:
                return _binary_search(middle_i + 1, end_i)
            return _binary_search(start_i, middle_i - 1)

        return _binary_search(0, len(nums) - 1)
