class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_sorted = sorted(nums)
        answer: list[list[int]] = []
        for fixed in range(len(nums_sorted) - 2):
            if fixed > 0 and nums_sorted[fixed] == nums_sorted[fixed - 1]:
                continue

            left = fixed + 1
            right = len(nums_sorted) - 1
            while left < right:
                total = nums_sorted[fixed] + nums_sorted[left] + nums_sorted[right]

                if total < 0:
                    left += 1
                    continue

                if total > 0:
                    right -= 1
                    continue

                answer.append(
                    [nums_sorted[fixed], nums_sorted[left], nums_sorted[right]]
                )
                while left < right and nums_sorted[left] == nums_sorted[left + 1]:
                    left += 1
                while left < right and nums_sorted[right] == nums_sorted[right - 1]:
                    right -= 1
                left += 1
                right -= 1

        return answer
