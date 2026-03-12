class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def generate_subsets(i: int, subset: list[int]) -> None:
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            generate_subsets(i + 1, subset)
            subset.pop()
            generate_subsets(i + 1, subset)

        generate_subsets(0, [])
        return result
