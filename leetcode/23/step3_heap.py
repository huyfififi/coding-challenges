import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_nodes = [(node.val, i) for i, node in enumerate(lists) if node is not None]
        heapq.heapify(min_nodes)

        dummy = ListNode()
        prev = dummy
        while min_nodes:
            _, i = heapq.heappop(min_nodes)
            min_node = lists[i]

            prev.next = min_node
            prev = min_node
            lists[i] = lists[i].next

            next_node = min_node.next
            if next_node is not None:
                heapq.heappush(min_nodes, (next_node.val, i))

        return dummy.next
