import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        negated_smallest = []

        def traverse(node: TreeNode | None) -> None:
            if node is None:
                return

            heapq.heappush(negated_smallest, -node.val)
            while len(negated_smallest) > k:
                heapq.heappop(negated_smallest)

            traverse(node.left)
            traverse(node.right)

        traverse(root)
        assert negated_smallest
        return -heapq.heappop(negated_smallest)
