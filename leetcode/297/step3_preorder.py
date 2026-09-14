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

            tokens.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.DELIMITER.join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        tokens = iter(data.split(self.DELIMITER))

        def build_tree() -> None:
            token = next(tokens)
            if token == self.NULL_NODE:
                return None

            node = TreeNode(int(token))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()
