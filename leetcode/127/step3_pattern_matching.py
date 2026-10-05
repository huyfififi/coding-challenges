import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        patten_to_words = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for wildcard_i in range(len(word)):
                patten_to_words[(word[:wildcard_i], word[wildcard_i + 1:])].append(
                    word
                )

        seen = {beginWord}
        frontier = [beginWord]
        distance = 1
        words = set(wordList)
        while frontier:
            next_frontier = []
            for word in frontier:
                if word == endWord:
                    return distance

                for wildcard_i in range(len(word)):
                    for neighbor in patten_to_words[
                        (word[:wildcard_i], word[wildcard_i + 1:])
                    ]:
                        if neighbor not in words:
                            continue
                        if neighbor in seen:
                            continue

                        seen.add(neighbor)
                        next_frontier.append(neighbor)

            distance += 1
            frontier = next_frontier

        return 0
