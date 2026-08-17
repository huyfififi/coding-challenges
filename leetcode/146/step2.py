from __future__ import annotations


class ListNode:
    def __init__(
        self,
        key: int | None = None,
        val: int | None = None,
        prev: ListNode | None = None,
        next: ListNode | None = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node: dict[int, ListNode] = {}

    def __detach_cache(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def __attach_cache(self, node: ListNode) -> None:
        most_recently_used = self.head.next
        most_recently_used.prev = node
        node.next = most_recently_used
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.__detach_cache(node)
        self.__attach_cache(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.__detach_cache(self.key_to_node[key])

        node = ListNode(key=key, val=value)
        self.__attach_cache(node)
        self.key_to_node[key] = node

        while len(self.key_to_node) > self.capacity:
            least_recently_used = self.tail.prev
            self.__detach_cache(least_recently_used)
            del self.key_to_node[least_recently_used.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
