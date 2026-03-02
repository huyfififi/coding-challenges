class Trie:
    class Node:
        def __init__(self) -> None:
            self.children = {}
            self.is_end = False

    def __init__(self) -> None:
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie.Node()
            node = node.children[letter]

        node.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        divisible = [False] * (len(s) + 1)
        divisible[0] = True

        for i in range(len(s)):
            if not divisible[i]:
                continue

            node = trie.root
            j = i
            while j < len(s):
                node = node.children.get(s[j])
                if node is None:
                    break

                if node.is_end:
                    divisible[j + 1] = True
                j += 1

        return divisible[len(s)]
