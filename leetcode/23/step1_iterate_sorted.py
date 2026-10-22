import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode()
        prev = dummy
        while True:
            min_node = ListNode(val=float("inf"))
            min_list_index = -1
            for i, node in enumerate(lists):
                if node is None:
                    continue

                if node.val < min_node.val:
                    min_node = node
                    min_list_index = i

            if math.isinf(min_node.val):
                return dummy.next

            prev.next = min_node
            prev = min_node
            lists[min_list_index] = lists[min_list_index].next
