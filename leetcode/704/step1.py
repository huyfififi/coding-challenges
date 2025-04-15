class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        left_i = 0
        right_i = len(nums) - 1

        while left_i <= right_i:
            middle_i = (left_i + right_i) // 2

            if nums[middle_i] == target:
                return middle_i

            if nums[middle_i] < target:
                left_i = middle_i + 1
                continue

            right_i = middle_i - 1

        return -1
