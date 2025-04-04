# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        merged_tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                merged_tail.next = list1
                merged_tail = merged_tail.next
                list1 = list1.next
            else:
                merged_tail.next = list2
                merged_tail = merged_tail.next
                list2 = list2.next

        while list1 is not None:
            merged_tail.next = list1
            merged_tail = merged_tail.next
            list1 = list1.next

        while list2 is not None:
            merged_tail.next = list2
            merged_tail = merged_tail.next
            list2 = list2.next

        return dummy.next
