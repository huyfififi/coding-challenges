# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None, lower_bound, upper_bound):
            if node is None:
                return True

            if not (lower_bound < node.val < upper_bound):
                return False

            return validate(node.left, lower_bound, node.val) and validate(
                node.right, node.val, upper_bound
            )

        return validate(root, float("-inf"), float("inf"))
