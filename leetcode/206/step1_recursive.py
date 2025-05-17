# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(
            node: Optional[ListNode],
        ) -> tuple[
            Optional[ListNode], Optional[ListNode]
        ]:  # reversed_tail, reversed_head
            if node is None:
                return None, None

            if node.next is None:
                return node, node

            reversed_tail, reversed_head = reverse_list_helper(node.next)
            reversed_tail.next = node
            node.next = None  # to avoid cycle at the end of the list

            return node, reversed_head

        return reverse_list_helper(head)[1]
