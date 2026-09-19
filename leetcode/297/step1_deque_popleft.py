import collections


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
                serialized.append(Codec.NULL_NODE)
                return

            serialized.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return Codec.DELIMITER.join(serialized)

    def deserialize(self, data):
        serialized = data.split(Codec.DELIMITER)
        serialized = collections.deque(serialized)

        def build_tree() -> TreeNode | None:
            """Returns the root of a re-constructed tree"""
            node_data = serialized.popleft()
            if node_data == Codec.NULL_NODE:
                return None

            node = TreeNode(int(node_data))
            node.left, node.right = build_tree(), build_tree()
            return node

        return build_tree()
