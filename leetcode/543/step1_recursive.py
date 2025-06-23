from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def check_diameter_and_max_depth(node: Optional[TreeNode]) -> tuple[int, int]:
            """returns diameter and max depth of the node's tree"""
            if node is None:
                return 0, 0

            left_diameter, left_max_depth = check_diameter_and_max_depth(node.left)
            right_diameter, right_max_depth = check_diameter_and_max_depth(node.right)

            return (
                max(
                    left_max_depth + right_max_depth, max(left_diameter, right_diameter)
                ),
                max(left_max_depth, right_max_depth) + 1,
            )

        return check_diameter_and_max_depth(root)[0]
