import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        seen = {beginWord}
        frontier = [beginWord]
        distance = 1
        while frontier:
            next_frontier = []
            for word in frontier:
                if word == endWord:
                    return distance

                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        characters = list(word)
                        characters[i] = c
                        neighbor = "".join(characters)
                        if neighbor in words and neighbor not in seen:
                            next_frontier.append(neighbor)
                            seen.add(neighbor)

            distance += 1
            frontier = next_frontier

        return 0
