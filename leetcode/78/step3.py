class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []

        def generate_subsets(i: int, subset: list[int]) -> None:
            if i == len(nums):
                all_subsets.append(subset.copy())
                return

            subset.append(nums[i])
            generate_subsets(i + 1, subset)
            subset.pop()
            generate_subsets(i + 1, subset)

        generate_subsets(0, [])
        return all_subsets
