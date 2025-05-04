# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        counter = 1
        while head:
            if counter > 10**4:
                return True
            head = head.next
            counter += 1
        return False
