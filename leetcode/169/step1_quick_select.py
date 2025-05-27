import random


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def partition(nums: list[int], left: int, right: int, pivot_index: int) -> int:
            pivot_value = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(nums: list[int], left: int, right: int, k: int) -> int:
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(nums, left, right, pivot_index)

            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return select(nums, left, pivot_index - 1, k)
            else:
                return select(nums, pivot_index + 1, right, k)

        def quickselect(nums: list[int], k: int) -> int:
            return select(nums, 0, len(nums) - 1, k)

        return quickselect(nums, len(nums) // 2)
