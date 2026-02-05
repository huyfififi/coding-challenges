class Solution:
    def sortColors(self, nums: list[int]) -> None:
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
                    swapped = True
