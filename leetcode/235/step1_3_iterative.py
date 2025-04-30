# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_q_low = min(p.val, q.val)
        p_q_high = max(p.val, q.val)

        while True:
            if root.val > p_q_high:
                root = root.left
                continue

            if root.val < p_q_low:
                root = root.right
                continue

            break

        return root
