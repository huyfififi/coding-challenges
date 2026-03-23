# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import dataclasses


@dataclasses.dataclass
class Span:
    begin: int
    end: int

    @property
    def size(self) -> int:
        return self.end - self.begin

    def is_empty(self) -> bool:
        return self.size <= 0


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        num_to_inorder_i = {num: i for i, num in enumerate(inorder)}

        def build_tree_helper(
            # preorder_span and inorder_span represent the same subtree
            preorder_span: Span,
            inorder_span: Span,
        ) -> TreeNode | None:
            if preorder_span.is_empty():
                return None

            root_val = preorder[preorder_span.begin]
            root_inorder_i = num_to_inorder_i[root_val]

            # When picking a root inorder index, the range is split into
            # [left subtree | root | right subtree]
            inorder_left = Span(inorder_span.begin, root_inorder_i)
            inorder_right = Span(root_inorder_i + 1, inorder_span.end)

            # [root | left subtree | right subtree]
            # The size of left subtree is determined by inorder left size
            preorder_left = Span(
                preorder_span.begin + 1, preorder_span.begin + 1 + inorder_left.size
            )
            preorder_right = Span(
                preorder_span.end - inorder_right.size, preorder_span.end
            )

            return TreeNode(
                val=root_val,
                left=build_tree_helper(preorder_left, inorder_left),
                right=build_tree_helper(preorder_right, inorder_right),
            )

        return build_tree_helper(Span(0, len(preorder)), Span(0, len(inorder)))
