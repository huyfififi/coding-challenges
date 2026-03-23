import string


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        source = s
        target = p
        if len(source) < len(target):
            return []

        anagram_length = len(target)

        target_char_counter = [0] * 26
        for letter in target:
            target_char_counter[string.ascii_lowercase.find(letter)] += 1

        sub_source_char_counter = [0] * 26
        for i in range(anagram_length):
            sub_source_char_counter[string.ascii_lowercase.find(source[i])] += 1

        anagram_start_indexes: list[int] = []
        for checking_start in range(len(source) - anagram_length + 1):
            if sub_source_char_counter == target_char_counter:
                anagram_start_indexes.append(checking_start)

            if checking_start < len(source) - anagram_length:
                sub_source_char_counter[
                    string.ascii_lowercase.find(source[checking_start])
                ] -= 1
                sub_source_char_counter[
                    string.ascii_lowercase.find(source[checking_start + anagram_length])
                ] += 1

        return anagram_start_indexes
