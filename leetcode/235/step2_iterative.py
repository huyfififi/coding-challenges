# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        while True:
            if root.val > max(p.val, q.val):
                root = root.left
                continue
            if root.val < min(p.val, q.val):
                root = root.right
                continue
            return root
