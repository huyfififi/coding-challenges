import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        pattern_to_words = collections.defaultdict(list)
        words = wordList.copy()
        words.append(beginWord)
        for word in words:
            for wildcard_i in range(len(word)):
                pattern_to_words[(word[:wildcard_i], word[wildcard_i + 1 :])].append(
                    word
                )

        distance = 1
        checking = [beginWord]
        seen = {beginWord}
        while checking:
            next_checking = []
            for word in checking:
                if word == endWord:
                    return distance

                for wildcard_i in range(len(word)):
                    for neighbor in pattern_to_words[
                        (word[:wildcard_i], word[wildcard_i + 1 :])
                    ]:
                        if neighbor in seen:
                            continue
                        next_checking.append(neighbor)
                        seen.add(neighbor)

            distance += 1
            checking = next_checking

        return 0
