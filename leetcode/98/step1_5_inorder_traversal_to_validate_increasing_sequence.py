# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = float("-inf")

        def traverse(node: TreeNode | None) -> bool:
            nonlocal prev

            if node is None:
                return True

            if not traverse(node.left):
                return False

            if node.val <= prev:
                return False
            prev = node.val

            return traverse(node.right)

        return traverse(root)
