# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        node_and_ranges = []
        node_and_ranges.append((root, float("-inf"), float("inf")))
        while node_and_ranges:
            node, lower_bound, upper_bound = node_and_ranges.pop()
            if node is None:
                continue
            if not (lower_bound < node.val < upper_bound):
                return False

            node_and_ranges.append((node.left, lower_bound, node.val))
            node_and_ranges.append((node.right, node.val, upper_bound))

        return True
