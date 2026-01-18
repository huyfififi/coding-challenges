# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None) -> tuple[bool, int | float, int | float]:
            """Returns (is valid BST, minimum value in tree, maximum value in tree)"""
            if node is None:
                return True, float("inf"), float("-inf")

            left_is_valid, left_min, left_max = validate(node.left)
            right_is_valid, right_min, right_max = validate(node.right)
            return (
                left_is_valid and right_is_valid and (left_max < node.val < right_min),
                min(left_min, node.val, right_min),
                max(left_max, node.val, right_max),
            )

        return validate(root)[0]
