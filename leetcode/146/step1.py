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
        self.tail = None
        self.key_to_node: dict[int, ListNode] = {}

    def __detach_cache(self, node: ListNode) -> None:
        if self.tail is node:
            self.tail = self.tail.prev

        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.next = None
        node.prev = None

        del self.key_to_node[node.key]

    def __attach_cache(self, node: ListNode) -> None:
        most_recently_used = self.head.next
        if most_recently_used is not None:
            most_recently_used.prev = node
            node.next = most_recently_used

        node.prev = self.head
        self.head.next = node
        if node.next is None:
            self.tail = node

        self.key_to_node[node.key] = node

        while len(self.key_to_node) > self.capacity:
            self.__detach_cache(self.tail)

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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
