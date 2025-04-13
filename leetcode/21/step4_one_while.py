# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def node_to_val(node: ListNode) -> int:
            return float("inf") if node is None else node.val

        dummy = ListNode()
        tail = dummy

        while list1 is not None or list2 is not None:
            if node_to_val(list1) < node_to_val(list2):
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        return dummy.next
