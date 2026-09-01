from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
        size: int = 1,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.size = size


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(val=val)
            return

        node = self.root
        while node is not None:
            node.size += 1
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val=val)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val=val)
                    return
                else:
                    node = node.right

    def delete(self, val: int) -> None:
        def delete_helper(root: TreeNode | None, val: int) -> TreeNode | None:
            """Returns the new root after deletion"""
            if root is None:
                return None

            if val < root.val:
                root.left = delete_helper(root.left, val)
                root.size -= 1
            elif root.val < val:
                root.right = delete_helper(root.right, val)
                root.size -= 1
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left

                successor = root.right
                while successor.left is not None:
                    successor = successor.left

                root.val = successor.val
                root.right = delete_helper(root.right, successor.val)
                root.size -= 1

            return root

        self.root = delete_helper(self.root, val)

    def find_kth_smallest(self, k: int) -> int | None:
        node = self.root
        offset = 0
        while node is not None:
            left_size = offset + (node.left.size if node.left is not None else 0)
            if left_size + 1 == k:
                return node.val
            elif k < left_size + 1:
                node = node.left
            else:
                offset = left_size + 1
                node = node.right

        return None


# See test_follow_up.py for tests.
