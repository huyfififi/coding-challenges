class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)

        answer: set[tuple[int, int, int]] = set()
        for fixed_index in range(len(sorted_nums) - 2):
            fixed_number = sorted_nums[fixed_index]

            left = fixed_index + 1
            right = len(sorted_nums) - 1
            while left < right:
                left_number = sorted_nums[left]
                right_number = sorted_nums[right]
                total = fixed_number + left_number + right_number
                if total == 0:
                    answer.add((fixed_number, left_number, right_number))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return list(map(list, answer))
