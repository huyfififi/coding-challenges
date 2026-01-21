class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def generate_permutations(remaining: list[int], generating: list[int]) -> None:
            if not remaining:
                permutations.append(generating)

            for i in range(len(remaining)):
                generate_permutations(
                    remaining[:i] + remaining[i + 1 :],
                    generating + [remaining[i]],
                )

        generate_permutations(nums, [])
        return permutations
