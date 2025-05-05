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
        ) -> tuple[int, bool]:  # height, is_balanced
            if node is None:
                return 0, True

            left_height, left_is_balanced = is_balanced_helper(node.left)
            right_height, right_is_balanced = is_balanced_helper(node.right)

            height = max(left_height, right_height) + 1
            _is_balanced = (
                left_is_balanced
                and right_is_balanced
                and abs(left_height - right_height) <= 1
            )
            return height, _is_balanced

        return is_balanced_helper(root)[1]
