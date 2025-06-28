# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        node_to_max_depth: dict[TreeNode | None, int] = {None: 0}
        node_and_visited_stack: list[tuple[TreeNode | None, bool]] = [(root, False)]

        while node_and_visited_stack:
            node, visited = node_and_visited_stack.pop()
            if node is None:
                continue

            if not visited:
                node_and_visited_stack.append((node, True))
                node_and_visited_stack.append((node.left, False))
                node_and_visited_stack.append((node.right, False))
                continue

            left_max_depth = node_to_max_depth[node.left]
            right_max_depth = node_to_max_depth[node.right]
            node_to_max_depth[node] = max(left_max_depth, right_max_depth) + 1

        return node_to_max_depth[root]
