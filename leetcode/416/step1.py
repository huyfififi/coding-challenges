class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        half_sum = sum_ // 2

        possible = [False] * (half_sum + 1)
        possible[0] = True

        for num in nums:
            for i in range(half_sum - 1, -1, -1):
                if not possible[i]:
                    continue

                if i + num > half_sum:
                    continue

                possible[i + num] = True

        return possible[half_sum]
