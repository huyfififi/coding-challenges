class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(1, len(nums)):
            num_to_insert = nums[i]
            j = i
            while j > 0 and nums[j - 1] > num_to_insert:
                nums[j] = nums[j - 1]
                j -= 1

            nums[j] = num_to_insert
