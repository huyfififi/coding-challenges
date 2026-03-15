# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        rightmost_values = []

        def traverse_and_store_rightmost(node: TreeNode | None, depth: int) -> None:
            if node is None:
                return

            if depth == len(rightmost_values):
                rightmost_values.append(node.val)

            traverse_and_store_rightmost(node.right, depth + 1)
            traverse_and_store_rightmost(node.left, depth + 1)

        traverse_and_store_rightmost(root, 0)
        return rightmost_values
