# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_valid(node: TreeNode | None, lower_bound, upper_bound):
            if node is None:
                return True

            if not (lower_bound < node.val < upper_bound):
                return False

            return is_valid(node.left, lower_bound, node.val) and is_valid(
                node.right, node.val, upper_bound
            )

        return is_valid(root, float("-inf"), float("inf"))
