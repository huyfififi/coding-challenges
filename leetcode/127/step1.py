import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        count = 1
        seen = {beginWord}
        candidates = [beginWord]
        words = set(wordList)
        while candidates:
            next_candidates = []
            for candidate in candidates:
                if candidate == endWord:
                    return count

                for i in range(len(candidate)):
                    neighbors = []
                    for c in string.ascii_lowercase:
                        neighbor = list(candidate)
                        neighbor[i] = c
                        neighbor = "".join(neighbor)
                        if neighbor != candidate:
                            neighbors.append(neighbor)

                    for neighbor in neighbors:
                        if neighbor in words and neighbor not in seen:
                            next_candidates.append(neighbor)
                            seen.add(neighbor)

            candidates = next_candidates
            count += 1

        return 0
