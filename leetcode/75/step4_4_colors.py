import random


# How about I add one more pointer?
# [2, 0, 2, 1, 1, 3], zero_end = 0, two_start = 5, three_start = 6
# [3, 0, 2, 1, 1, 2], zero_end = 0, two_start = 5, three_start = 6
# [1, 0, 2, 1, 2, 3], zero_end = 0, two_start = 4, three_start = 5


def sort_colors(nums: list[int]) -> None:
    zero_end = 0  # i < zero -> nums[i] == 0
    two_start = len(nums) - 1  # two_start < i <= three_start -> nums[i] == 2
    three_start = len(nums) - 1  # three_start < i -> nums[i] == 3

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


test_cases = [
    # 3 colors
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
    # 4 colors
    [1, 0, 2, 3],
    [3, 2, 1, 0],
    [2, 0, 2, 3, 1, 1, 0, 3],
]
# random test cases
test_cases += [[random.randint(0, 3) for _ in range(10)] for _ in range(10)]

for test_case in test_cases:
    colors = test_case.copy()
    sort_colors(colors)
    assert colors == sorted(test_case)
