# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow_runner = head
        fast_runner = head.next

        while slow_runner is not fast_runner:
            if fast_runner is None or fast_runner.next is None:
                return False
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next

        return True
