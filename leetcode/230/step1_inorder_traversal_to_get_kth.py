class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0

        def find_kth_smallest(node: TreeNode | None) -> int | None:
            if node is None:
                return None

            nonlocal count

            kth_smallest = find_kth_smallest(node.left)
            if kth_smallest is not None:
                return kth_smallest

            count += 1
            if count == k:
                return node.val

            return find_kth_smallest(node.right)

        return find_kth_smallest(root)
