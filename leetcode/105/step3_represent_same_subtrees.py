# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Span:
    def __init__(self, begin: int, end: int) -> None:
        self.begin = begin
        self.end = end

    @property
    def size(self) -> int:
        return max(self.end - self.begin, 0)

    @property
    def is_empty(self) -> bool:
        return self.size == 0


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        val_to_inorder_index = {val: index for index, val in enumerate(inorder)}

        def build_tree_helper(
            preorder_span: Span, inorder_span: Span
        ) -> TreeNode | None:
            assert preorder_span.size == inorder_span.size
            if preorder_span.is_empty:
                return None

            root_preorder_index = preorder_span.begin
            root_val = preorder[root_preorder_index]
            root_inorder_index = val_to_inorder_index[root_val]

            inorder_left = Span(inorder_span.begin, root_inorder_index)
            preorder_left = Span(
                preorder_span.begin + 1, preorder_span.begin + 1 + inorder_left.size
            )

            inorder_right = Span(root_inorder_index + 1, inorder_span.end)
            preorder_right = Span(
                preorder_span.begin + 1 + preorder_left.size, preorder_span.end
            )

            return TreeNode(
                val=root_val,
                left=build_tree_helper(preorder_left, inorder_left),
                right=build_tree_helper(preorder_right, inorder_right),
            )

        return build_tree_helper(Span(0, len(preorder)), Span(0, len(inorder)))
