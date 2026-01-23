import collections


class TimeMap:
    def __init__(self):
        self.key_to_value_and_timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_and_timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_and_timestamps = self.key_to_value_and_timestamps[key]

        low = 0  # everything before low is <= timestamp
        high = len(value_and_timestamps)  # everything after high is > timestamp
        while low < high:
            middle = (low + high) // 2
            if timestamp < value_and_timestamps[middle][1]:
                high = middle
            else:
                low = middle + 1

        if low == 0:
            return ""
        return value_and_timestamps[low - 1][0]
