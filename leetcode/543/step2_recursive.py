from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculate_diameter_and_height(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return 0, 0

            left_diameter, left_height = calculate_diameter_and_height(node.left)
            right_diameter, right_height = calculate_diameter_and_height(node.right)

            return (
                max(left_height + right_height, left_diameter, right_diameter),
                max(left_height, right_height) + 1,
            )

        return calculate_diameter_and_height(root)[0]
