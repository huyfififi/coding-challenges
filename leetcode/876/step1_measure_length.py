# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        list_length = 0
        node = head
        while node is not None:
            list_length += 1
            node = node.next

        move_count_to_middle = list_length // 2
        node = head
        for _ in range(move_count_to_middle):
            node = node.next

        return node
