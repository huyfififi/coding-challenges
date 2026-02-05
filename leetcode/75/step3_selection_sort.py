class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]
