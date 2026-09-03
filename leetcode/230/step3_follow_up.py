from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int,
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
        def insert_helper(root: TreeNode | None, val: int) -> TreeNode:
            """Returns the new root after insertion"""
            if root is None:
                return TreeNode(val=val)

            root.size += 1
            if val < root.val:
                root.left = insert_helper(root.left, val)
            elif root.val < val:
                root.right = insert_helper(root.right, val)
            else:
                raise ValueError("The value already exists in the tree.")

            return root

        self.root = insert_helper(self.root, val)

    def delete(self, val: int) -> None:
        def delete_helper(root: TreeNode | None, val: int) -> TreeNode | None:
            """Returns the new root after deletion"""
            if root is None:
                return None

            root.size -= 1
            if val < root.val:
                root.left = delete_helper(root.left, val)
            elif root.val < val:
                root.right = delete_helper(root.right, val)
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

            return root

        self.root = delete_helper(self.root, val)

    def find_kth_smallest(self, k: int) -> int | None:
        def find_kth_smallest_helper(root: TreeNode | None, k: int) -> int | None:
            if root is None:
                return None

            left_size = root.left.size if root.left is not None else 0
            if left_size + 1 == k:
                return root.val
            if k < left_size + 1:
                return find_kth_smallest_helper(root.left, k)
            return find_kth_smallest_helper(root.right, k - (left_size + 1))

        return find_kth_smallest_helper(self.root, k)
