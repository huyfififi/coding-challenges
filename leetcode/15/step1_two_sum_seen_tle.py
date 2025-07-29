class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer: set[tuple[int, int, int]] = set()
        for fixed_index in range(len(nums) - 2):
            fixed_number = nums[fixed_index]

            seen: set[int] = set()
            for index in range(fixed_index + 1, len(nums)):
                number = nums[index]
                complement = -(fixed_number + number)
                if complement in seen:
                    answer.add(tuple(sorted([fixed_number, number, complement])))
                seen.add(number)

        return list(map(list, answer))
