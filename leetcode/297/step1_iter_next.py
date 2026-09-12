class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


DELIMITER = ","
NULL_NODE = "#"


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        serialized: list[str] = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                serialized.append(NULL_NODE)
                return

            serialized.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return DELIMITER.join(serialized)

    def deserialize(self, data):
        serialized = iter(data.split(DELIMITER))

        def build_tree() -> TreeNode | None:
            """Returns the new root"""
            node_data = next(serialized)
            if node_data == NULL_NODE:
                return None

            node = TreeNode(int(node_data))
            node.left, node.right = build_tree(), build_tree()
            return node

        return build_tree()
