class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def generate_permutations(remaining: list[int], prefix: list[int]) -> None:
            if not remaining:
                permutations.append(prefix.copy())
                return

            for i in range(len(remaining)):
                picked = remaining.pop(i)
                prefix.append(picked)

                generate_permutations(remaining, prefix)

                remaining.insert(i, picked)
                prefix.pop()

        generate_permutations(nums.copy(), [])
        return permutations
