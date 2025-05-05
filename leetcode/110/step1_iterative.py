# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Post-order traversal
        # First visit: the node is used to push direct children to a stack
        # Second visit: both children have been processed, so we can check the node's height balance

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
            if abs(node_to_height[node.left] - node_to_height[node.right]) > 1:
                return False
            height = max(left_height, right_height) + 1
            node_to_height[node] = height

        return True
