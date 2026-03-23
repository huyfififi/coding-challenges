# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TrreeNode | None:
        if not preorder or not inorder:
            return None

        val_to_inorder_index = {num: i for i, num in enumerate(inorder)}

        def build_tree_helper(
            preorder_index: int, inorder_begin: int, inorder_end: int
        ) -> tuple[TreeNode | None, int]:
            node = TreeNode(preorder[preorder_index])
            preorder_index += 1
            inorder_index = val_to_inorder_index[node.val]
            if inorder_begin <= inorder_index - 1:
                node.left, preorder_index = build_tree_helper(
                    preorder_index, inorder_begin, inorder_index - 1
                )
            if inorder_index + 1 <= inorder_end:
                node.right, preorder_index = build_tree_helper(
                    preorder_index, inorder_index + 1, inorder_end
                )

            return node, preorder_index

        return build_tree_helper(0, 0, len(inorder) - 1)[0]
