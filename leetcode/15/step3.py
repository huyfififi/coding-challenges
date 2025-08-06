class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer: list[list[int]] = []
        for fixed in range(len(nums) - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            left = fixed + 1
            right = len(nums) - 1
            while left < right:
                total = nums[fixed] + nums[left] + nums[right]

                if total == 0:
                    answer.append([nums[fixed], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    continue

                if total < 0:
                    left += 1
                    continue

                right -= 1

        return answer
