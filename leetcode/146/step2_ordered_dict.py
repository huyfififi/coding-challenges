import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        self.key_to_val.move_to_end(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        self.key_to_val.pop(key, default=None)
        self.key_to_val[key] = value

        while len(self.key_to_val) > self.capacity:
            self.key_to_val.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
