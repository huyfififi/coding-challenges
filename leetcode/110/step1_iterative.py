# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node_to_results = {None: (0, True)}  # {node: (depth, is_balanced)}
        stack = [(root, False)]  # [(node, visited)]

        while stack:
            node, visited = stack.pop()

            if node in node_to_results:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue

            left_depth, left_is_balanced = node_to_results[node.left]
            right_depth, right_is_balanced = node_to_results[node.right]
            depth = max(left_depth, right_depth) + 1
            is_balanced = (
                left_is_balanced
                and right_is_balanced
                and abs(left_depth - right_depth) <= 1
            )
            node_to_results[node] = (depth, is_balanced)

        return node_to_results[root][1]
