class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_to_characters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def generate_combinations(
            digit_index: int, generating: list[str], generated: list[str]
        ) -> None:
            if digit_index == len(digits):
                generated.append("".join(generating))
                return

            for ch in digit_to_characters[digits[digit_index]]:
                generating.append(ch)
                generate_combinations(digit_index + 1, generating, generated)
                generating.pop()

        generated = []
        generate_combinations(0, [], generated)
        return generated
