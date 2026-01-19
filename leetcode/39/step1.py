class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        total_and_combinations: list[tuple[int, list[int]]] = [(0, [])]
        combinations_found: set[tuple[int, ...]] = set()

        while total_and_combinations:
            total, combination = total_and_combinations.pop()
            if total < target:
                for candidate in candidates:
                    total_and_combinations.append(
                        (total + candidate, combination + [candidate])
                    )
                continue

            if target < total:
                continue

            sorted_combination = tuple(sorted(combination))
            if sorted_combination not in combinations_found:
                combinations_found.add(sorted_combination)

        return list(map(list, combinations_found))
