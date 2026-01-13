class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        target_combinations: list[list[int]] = []
        num_candidates = len(candidates)
        sorted_candidates = sorted(candidates)

        def find_target_combinations(
            candidate_start: int, total: int, combination: list[int]
        ) -> None:
            if total == target:
                target_combinations.append(combination.copy())
                return

            for i in range(candidate_start, num_candidates):
                new_total = total + sorted_candidates[i]
                if new_total > target:
                    return

                combination.append(sorted_candidates[i])
                find_target_combinations(i, new_total, combination)
                combination.pop()

        find_target_combinations(0, 0, [])
        return target_combinations
