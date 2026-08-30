class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0

        def traverse(
            node: TreeNode | None,
        ) -> tuple[int | None, bool]:  # kth smallest, found
            if node is None:
                return None, False

            nonlocal count

            kth_smallest, found = traverse(node.left)
            if found:
                return kth_smallest, True

            count += 1
            if count == k:
                return node.val, True

            return traverse(node.right)

        return traverse(root)[0]
