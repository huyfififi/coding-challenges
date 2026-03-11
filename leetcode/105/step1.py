# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def build_tree_helper(pre_i: int, in_i: int, in_end: int) -> TreeNode | None:
            if in_end <= in_i:
                return None

            try:
                matching_in_i = inorder.index(preorder[pre_i], in_i, in_end)
            except ValueError:
                return build_tree_helper(pre_i + 1, in_i, in_end)

            return TreeNode(
                val=inorder[matching_in_i],
                left=build_tree_helper(pre_i + 1, in_i, matching_in_i),
                right=build_tree_helper(pre_i + 1, matching_in_i + 1, in_end),
            )

        return build_tree_helper(0, 0, len(inorder))
