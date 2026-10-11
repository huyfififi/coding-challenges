import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        patten_to_words = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                patten_to_words[(word[:i], word[i + 1 :])].append(word)

        frontier = [beginWord]
        seen = {beginWord}
        distance = 1
        while frontier:
            next_frontier = []
            for word in frontier:
                if word == endWord:
                    return distance

                for i in range(len(word)):
                    for neighbor in patten_to_words[(word[:i], word[i + 1 :])]:
                        if neighbor in seen:
                            continue

                        next_frontier.append(neighbor)
                        seen.add(neighbor)

            distance += 1
            frontier = next_frontier

        return 0
