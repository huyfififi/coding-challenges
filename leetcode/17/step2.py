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

        generated = []

        def generate_combinations(digit_index: int, generating: list[str]) -> None:
            if digit_index == len(digits):
                generated.append("".join(generating))
                return

            for character in digit_to_characters[digits[digit_index]]:
                generating.append(character)
                generate_combinations(digit_index + 1, generating)
                generating.pop()

        generate_combinations(0, [])
        return generated
