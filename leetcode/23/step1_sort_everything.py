class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        merged = []
        for node in lists:
            while node is not None:
                merged.append(node)
                node = node.next

        if not merged:
            return None

        merged.sort(key=lambda node: node.val)
        root = merged[0]
        for i in range(len(merged) - 1):
            merged[i].next = merged[i + 1]
        merged[-1].next = None

        return root
