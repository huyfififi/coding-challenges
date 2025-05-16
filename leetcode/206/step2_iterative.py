# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None
        node = head

        while node:
            next_node_to_reverse = node.next

            node.next = reversed_head

            reversed_head = node
            node = next_node_to_reverse

        return reversed_head
