class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Solution without relying on the collections module
        necessary_characters: dict[str, int] = {}
        available_characters: dict[str, int] = {}

        for c in ransomNote:
            if c not in necessary_characters:
                necessary_characters[c] = 1
            else:
                necessary_characters[c] += 1

        for c in magazine:
            if c not in available_characters:
                available_characters[c] = 1
            else:
                available_characters[c] += 1

        for necessary_character, count in necessary_characters.items():
            if count > available_characters.get(necessary_character, 0):
                return False

        return True
