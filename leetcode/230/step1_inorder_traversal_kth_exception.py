class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0

        class Found(Exception):
            def __init__(self, val: int) -> None:
                self.val = val

        def traverse(node: TreeNode | None) -> None:
            nonlocal count

            if node is None:
                return

            traverse(node.left)
            count += 1
            if count == k:
                raise Found(node.val)
            traverse(node.right)

        try:
            traverse(root)
        except Found as e:
            return e.val
