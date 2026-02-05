class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for last in range(len(nums) - 1, 0, -1):
            for i in range(last):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
