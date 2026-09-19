class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


DELIMITER = ","
NULL_NODE = "#"


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
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

    def deserialize(self, data: str) -> TreeNode | None:
        nodes = data.split(DELIMITER)

        def build_tree(node_i: int) -> TreeNode | int:
            """Returns root and next node index"""
            if nodes[node_i] == NULL_NODE:
                return None, node_i + 1

            node = TreeNode(int(nodes[node_i]))
            left, next_i = build_tree(node_i + 1)
            right, next_i = build_tree(next_i)
            node.left, node.right = left, right
            return node, next_i

        return build_tree(0)[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
