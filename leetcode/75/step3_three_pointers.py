class Solution:
    def sortColors(self, nums: list[int]) -> None:
        RED = 0
        BLUE = 2

        red_end = 0  # i < red_end: nums[i] == RED
        blue_start = len(nums) - 1  # blue_start < i: nums[i] == BLUE
        i = 0
        while i <= blue_start:
            if nums[i] == RED:
                nums[i], nums[red_end] = nums[red_end], nums[i]
                red_end += 1
                i += 1
            elif nums[i] == BLUE:
                nums[i], nums[blue_start] = nums[blue_start], nums[i]
                blue_start -= 1
            else:
                i += 1
