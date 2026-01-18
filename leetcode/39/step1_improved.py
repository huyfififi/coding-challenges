class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        target_combinations = []

        def find_target_combinations(
            min_candidate_index: int, total: int, combination: list[int]
        ) -> None:
            if total == target:
                target_combinations.append(combination.copy())
                return

            if total > target:
                return

            for i in range(min_candidate_index, len(candidates)):
                combination.append(candidates[i])
                find_target_combinations(
                    i,
                    total + candidates[i],
                    combination,
                )
                combination.pop()

        find_target_combinations(0, 0, [])
        return target_combinations
