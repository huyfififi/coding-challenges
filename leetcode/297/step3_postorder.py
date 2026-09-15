class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    DELIMITER = ","
    NULL_NODE = "#"

    def serialize(self, root: TreeNode | None) -> str:
        tokens = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                tokens.append(self.NULL_NODE)
                return

            traverse(node.left)
            traverse(node.right)
            tokens.append(str(node.val))

        traverse(root)
        return self.DELIMITER.join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        tokens = data.split(self.DELIMITER)

        def build_tree() -> TreeNode | None:
            token = tokens.pop()
            if token == self.NULL_NODE:
                return None

            node = TreeNode(int(token))
            node.right = build_tree()
            node.left = build_tree()
            return node

        return build_tree()
