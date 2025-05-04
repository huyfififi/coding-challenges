# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        node = head

        while node is not None:
            if node in visited_nodes:
                return True
            visited_nodes.add(node)
            node = node.next

        return False
