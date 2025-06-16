import random


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def quickselect(nums: list[int], left: int, right: int, k: int) -> int:
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_value = nums[pivot_index]
            store_index = left
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[store_index], nums[right] = nums[right], nums[store_index]

            if store_index == k:
                return nums[store_index]
            elif store_index < k:
                return quickselect(nums, store_index + 1, right, k)
            else:
                return quickselect(nums, left, store_index - 1, k)

        return quickselect(nums, 0, len(nums) - 1, len(nums) // 2)
