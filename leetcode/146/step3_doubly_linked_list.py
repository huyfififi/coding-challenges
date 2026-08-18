from __future__ import annotations


class ListNode:
    def __init__(
        self,
        key: int | None = None,
        value: int | None = None,
        next_: ListNode | None = None,
        prev: ListNode | None = None,
    ):
        self.key = key
        self.value = value
        self.next = next_
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node: dict[int, ListNode] = {}

    def __detach_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def __attach_node(self, node: ListNode) -> None:
        most_recent = self.head.next
        self.head.next = node
        node.prev = self.head
        most_recent.prev = node
        node.next = most_recent

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.__detach_node(node)
        self.__attach_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.__detach_node(node)
            node.value = value
        else:
            node = ListNode(key=key, value=value)
            self.key_to_node[key] = node

        self.__attach_node(node)

        while len(self.key_to_node) > self.capacity:
            least_recent = self.tail.prev
            self.__detach_node(least_recent)
            del self.key_to_node[least_recent.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
