class Trie:
    WORD_END = "$"

    class TrieNode:
        def __init__(self, letter: str):
            self.letter = letter
            self.child_letter_to_node = {}

    def __init__(self):
        self.root = Trie.TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.child_letter_to_node:
                new_child = Trie.TrieNode(letter=letter)
                node.child_letter_to_node[letter] = new_child
                node = new_child
            else:
                node = node.child_letter_to_node[letter]

        node.child_letter_to_node[Trie.WORD_END] = Trie.TrieNode(letter=Trie.WORD_END)

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.child_letter_to_node:
                return False
            node = node.child_letter_to_node[letter]
        return Trie.WORD_END in node.child_letter_to_node

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
