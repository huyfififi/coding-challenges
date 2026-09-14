class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    DELIMITER = ","
    NULL_NODE = "#"

    def serialize(self, root: TreeNode | None) -> str:
        serialized: list[str] = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                serialized.append(self.NULL_NODE)
                return

            serialized.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.DELIMITER.join(serialized)

    def deserialize(self, data: str) -> TreeNode | None:
        serialized = iter(data.split(self.DELIMITER))

        def build_tree() -> TreeNode | None:
            """
            Builds and returns the root of the next subtree,
            consuming tokens in preorder.
            """
            node_data = next(serialized)
            if node_data == self.NULL_NODE:
                return None

            node = TreeNode(int(node_data))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()
