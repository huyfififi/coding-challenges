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
        ) -> tuple[int, bool]:  # depth, is_balanced
            if node is None:
                return 0, True

            left_depth, left_is_balanced = is_balanced_helper(node.left)
            right_depth, right_is_balanced = is_balanced_helper(node.right)

            depth = max(left_depth, right_depth) + 1
            _is_balanced = (
                left_is_balanced
                and right_is_balanced
                and abs(left_depth - right_depth) <= 1
            )
            return depth, _is_balanced

        return is_balanced_helper(root)[1]
