class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(1, len(nums)):
            num_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > num_to_insert:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = num_to_insert
