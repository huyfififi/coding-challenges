import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = wordList.copy()
        words.append(beginWord)

        def are_neighbors(s1: str, s2: str) -> bool:
            assert len(s1) == len(s2)

            diff_count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff_count += 1

                if 2 <= diff_count:
                    return False

            return diff_count == 1

        word_to_neighbors = collections.defaultdict(list)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if are_neighbors(words[i], words[j]):
                    word_to_neighbors[words[i]].append(words[j])
                    word_to_neighbors[words[j]].append(words[i])

        count = 1
        seen = set()
        candidates = [beginWord]
        while candidates:
            next_candidates = set()
            for candidate in candidates:
                if candidate == endWord:
                    return count

                seen.add(candidate)
                for neighbor in word_to_neighbors[candidate]:
                    if neighbor in seen:
                        continue

                    next_candidates.add(neighbor)

            candidates = list(next_candidates)
            count += 1

        return 0
