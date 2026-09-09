# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized: list[str] = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                serialized.append("#")
                return

            serialized.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return ",".join(serialized)

    def deserialize(self, data: str) -> TreeNode | None:
        raise NotImplementedError("TODO")


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
