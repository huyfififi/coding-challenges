class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        half_sum = sum_ // 2

        found = False

        def find_target_subset(subset_sum: int, checking: int) -> None:
            nonlocal found

            if checking == len(nums):
                return

            if subset_sum == half_sum:
                found |= True
                return

            if subset_sum > half_sum:
                return

            find_target_subset(subset_sum, checking + 1)
            find_target_subset(subset_sum + nums[checking], checking + 1)

        find_target_subset(0, 0)
        return found
