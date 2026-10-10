import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        words = [beginWord]
        seen = {beginWord}
        distance = 1
        while words:
            next_words = []
            for word in words:
                if word == endWord:
                    return distance

                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        characters = list(word)
                        characters[i] = c
                        neighbor = "".join(characters)
                        if neighbor in word_set and neighbor not in seen:
                            next_words.append(neighbor)
                            seen.add(neighbor)

            distance += 1
            words = next_words

        return 0
