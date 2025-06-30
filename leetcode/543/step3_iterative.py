# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        node_to_diameter_and_height = {None: (0, 0)}
        node_and_visited_stack = [(root, False)]

        while node_and_visited_stack:
            node, visited = node_and_visited_stack.pop()
            if node is None:
                continue

            if not visited:
                node_and_visited_stack.append((node, True))
                node_and_visited_stack.append((node.left, False))
                node_and_visited_stack.append((node.right, False))
                continue

            left_diameter, left_height = node_to_diameter_and_height[node.left]
            right_diameter, right_height = node_to_diameter_and_height[node.right]

            diameter = max(left_height + right_height, left_diameter, right_diameter)
            height = max(left_height, right_height) + 1
            node_to_diameter_and_height[node] = (diameter, height)

        return node_to_diameter_and_height[root][0]
