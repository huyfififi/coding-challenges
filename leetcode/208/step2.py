class Trie:
    class TrieNode:
        def __init__(self):
            self.child_letter_to_node = {}
            self.is_end = False

    def __init__(self):
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.child_letter_to_node:
                node.child_letter_to_node[letter] = Trie.TrieNode()
            node = node.child_letter_to_node[letter]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.child_letter_to_node:
                return False
            node = node.child_letter_to_node[letter]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.child_letter_to_node:
                return False
            node = node.child_letter_to_node[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
