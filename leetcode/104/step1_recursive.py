# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return max(left_max_depth, right_max_depth) + 1
