class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def create_permutations(used: list[bool], generating: list[int]) -> None:
            if len(generating) == len(nums):
                permutations.append(generating.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                generating.append(nums[i])

                create_permutations(used, generating)

                used[i] = False
                generating.pop()

        create_permutations([False] * len(nums), [])
        return permutations
