import random


def sort_colors(nums: list[int]) -> None:
    zero_end = 0  # i < zero: nums[i] == 0
    two_start = len(nums) - 1  # two_start < i <= three_start: nums[i] == 2
    three_start = len(nums) - 1  # three_start < i <= four_start: nums[i] == 3
    four_start = len(nums) - 1  # four_start < i: nums[i] == 4

    i = 0
    while i <= two_start:
        if nums[i] == 0:
            nums[i], nums[zero_end] = nums[zero_end], nums[i]
            zero_end += 1
            i += 1
            continue

        if nums[i] == 1:
            i += 1
            continue

        if nums[i] == 2:
            nums[i], nums[two_start] = nums[two_start], nums[i]
            two_start -= 1
            continue

        if nums[i] == 3:
            if i != two_start:
                nums[three_start], nums[two_start] = nums[two_start], nums[three_start]
            nums[i], nums[three_start] = nums[three_start], nums[i]
            two_start -= 1
            three_start -= 1
            continue

        if nums[i] == 4:
            if i != three_start:
                if i != two_start:
                    nums[three_start], nums[two_start] = (
                        nums[two_start],
                        nums[three_start],
                    )
                nums[four_start], nums[three_start] = (
                    nums[three_start],
                    nums[four_start],
                )
            nums[i], nums[four_start] = nums[four_start], nums[i]
            two_start -= 1
            three_start -= 1
            four_start -= 1


test_cases = [[random.randint(0, 4) for _ in range(20)] for _ in range(20)]

for test_case in test_cases:
    colors = test_case.copy()
    sort_colors(colors)
    assert colors == sorted(test_case)
