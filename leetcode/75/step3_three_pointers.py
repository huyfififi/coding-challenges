class Solution:
    def sortColors(self, nums: list[int]) -> None:
        RED = 0
        BLUE = 2

        red_end = 0  # i < red_end: nums[i] == RED
        blue_start = len(nums) - 1  # blue_start < i: nums[i] == BLUE
        checking = 0
        while checking <= blue_start:
            if nums[checking] == RED:
                nums[checking], nums[red_end] = nums[red_end], nums[checking]
                red_end += 1
                checking += 1
            elif nums[checking] == BLUE:
                nums[checking], nums[blue_start] = nums[blue_start], nums[checking]
                blue_start -= 1
            else:
                checking += 1
