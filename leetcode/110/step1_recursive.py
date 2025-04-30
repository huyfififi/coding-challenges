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
        ) -> tuple[int, bool]:  # (depth, is balanced) of a tree starting from node
            if node is None:
                return 0, True

            left_depth, left_is_balanced = is_balanced_helper(node.left)
            right_depth, right_is_balanced = is_balanced_helper(node.right)

            depth = max(left_depth, right_depth) + 1

            if not left_is_balanced or not right_is_balanced:
                return depth, False
            return depth, abs(left_depth - right_depth) <= 1

        return is_balanced_helper(root)[1]
