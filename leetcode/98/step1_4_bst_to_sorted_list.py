# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        values = []

        def traverse(node: TreeNode | None, values: list[int]) -> None:
            if node is None:
                return

            traverse(node.left, values)
            values.append(node.val)
            traverse(node.right, values)

        traverse(root, values)
        for i in range(len(values) - 1):
            if values[i] >= values[i + 1]:
                return False
        return True
