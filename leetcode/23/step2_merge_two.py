class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        node1 = self.mergeKLists(lists[: len(lists) // 2])
        node2 = self.mergeKLists(lists[len(lists) // 2 :])
        dummy = ListNode()
        prev = dummy
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                prev.next = node1
                prev = node1
                node1 = node1.next
            else:
                prev.next = node2
                prev = node2
                node2 = node2.next

        prev.next = node1 if node1 is not None else node2

        return dummy.next
