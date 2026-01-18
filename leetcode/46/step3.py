class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def create_permutations(remaining: list[int], prefix: list[int]) -> None:
            if not remaining:
                permutations.append(prefix.copy())
                return

            for i in range(len(remaining)):
                picked = remaining.pop(i)
                prefix.append(picked)

                create_permutations(remaining, prefix)

                remaining.insert(i, picked)
                prefix.pop()

        create_permutations(nums.copy(), [])
        return permutations
