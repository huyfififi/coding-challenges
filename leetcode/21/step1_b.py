# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        def splice(
            prev: ListNode, node1: ListNode | None, node2: ListNode | None
        ) -> None:
            if node1 is None:
                prev.next = node2
                return
            if node2 is None:
                prev.next = node1
                return

            if node1.val < node2.val:
                prev.next = node1
                splice(node1, node1.next, node2)
            else:
                prev.next = node2
                splice(node2, node1, node2.next)

        splice(dummy, list1, list2)
        return dummy.next
