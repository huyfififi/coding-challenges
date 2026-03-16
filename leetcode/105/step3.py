# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        value_to_inorder_index = {index: value for value, index in enumerate(inorder)}

        def build_tree_helper(
            root_preorder_index: int, inorder_begin: int, inorder_end: int
        ) -> tuple[TreeNode | None, int]:
            if inorder_end <= inorder_begin:
                return None, root_preorder_index

            root_val = preorder[root_preorder_index]
            root_inorder_index = value_to_inorder_index[root_val]

            next_root_preorder_index = root_preorder_index + 1

            left, next_root_preorder_index = build_tree_helper(
                next_root_preorder_index, inorder_begin, root_inorder_index
            )
            right, next_root_preorder_index = build_tree_helper(
                next_root_preorder_index, root_inorder_index + 1, inorder_end
            )

            return (
                TreeNode(val=root_val, left=left, right=right),
                next_root_preorder_index,
            )

        return build_tree_helper(0, 0, len(inorder))[0]
