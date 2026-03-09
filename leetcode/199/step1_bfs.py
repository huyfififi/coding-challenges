# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        rightmost_values = []
        nodes = [root]
        while nodes:
            next_nodes = []

            for i in range(len(nodes)):
                if i == len(nodes) - 1:
                    rightmost_values.append(nodes[i].val)

                if nodes[i].left is not None:
                    next_nodes.append(nodes[i].left)
                if nodes[i].right is not None:
                    next_nodes.append(nodes[i].right)

            nodes = next_nodes

        return rightmost_values
