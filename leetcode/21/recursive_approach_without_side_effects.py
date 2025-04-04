# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            dummy = ListNode()
            merged_tail = dummy
            while list2 is not None:
                merged_tail.next = ListNode(list2.val)
                merged_tail = merged_tail.next
                list2 = list2.next
            return dummy.next

        if list2 is None:
            dummy = ListNode()
            merged_tail = dummy
            while list1 is not None:
                merged_tail.next = ListNode(list1.val)
                merged_tail = merged_tail.next
                list1 = list1.next
            return dummy.next
    
        if list1.val < list2.val:
            head = ListNode(list1.val)
            head.next = self.mergeTwoLists(list1.next, list2)
            return head
        else:
            head = ListNode(list2.val)
            head.next = self.mergeTwoLists(list1, list2.next)
            return head
