class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        sorted_elements: list[int] = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                return

            traverse(node.left)
            sorted_elements.append(node.val)
            traverse(node.right)

        traverse(root)

        assert k <= len(sorted_elements)
        return sorted_elements[k - 1]
