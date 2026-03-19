class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_to_characters: dict[str, list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        all_combinations = []

        def generate_combinations(digit_index: int, combination: list[int]) -> None:
            if digit_index == len(digits):
                all_combinations.append("".join(combination))
                return

            for character in digit_to_characters[digits[digit_index]]:
                combination.append(character)
                generate_combinations(digit_index + 1, combination)
                combination.pop()

        generate_combinations(0, [])
        return all_combinations
