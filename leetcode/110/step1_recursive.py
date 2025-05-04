# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced_helper(
            node: Optional[TreeNode],
        ) -> tuple[int, bool]:  # (height, is balanced) of a tree starting from node
            if node is None:
                return 0, True

            left_height, left_is_balanced = is_balanced_helper(node.left)
            right_height, right_is_balanced = is_balanced_helper(node.right)

            height = max(left_height, right_height) + 1

            if not left_is_balanced or not right_is_balanced:
                return height, False
            return height, abs(left_height - right_height) <= 1

        return is_balanced_helper(root)[1]
