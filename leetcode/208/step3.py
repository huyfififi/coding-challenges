class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie.Node()
            node = node.children[letter]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
