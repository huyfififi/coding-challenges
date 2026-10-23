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
        count = 0
        while min_nodes:
            count += 1
            _, min_list_index = heapq.heappop(min_nodes)
            min_node = lists[min_list_index]
            prev.next = min_node
            prev = min_node

            next_node = min_node.next
            if next_node is not None:
                lists[min_list_index] = next_node
                heapq.heappush(min_nodes, (next_node.val, min_list_index))

        return dummy.next
