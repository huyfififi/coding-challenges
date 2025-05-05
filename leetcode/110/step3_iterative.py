# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node_to_height = {None: 0}
        stack = [(root, False)]  # [(node, visited)]

        while stack:
            node, visited = stack.pop()
            if node is None:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue

            left_height = node_to_height[node.left]
            right_height = node_to_height[node.right]
            if abs(left_height - right_height) > 1:
                return False

            node_to_height[node] = max(left_height, right_height) + 1

        return True
