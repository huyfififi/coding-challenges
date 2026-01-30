import collections


class TimeMap:
    def __init__(self):
        self.key_to_value_and_timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_and_timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_and_timestamps = self.key_to_value_and_timestamps[key]

        low = 0
        high = len(value_and_timestamps) - 1
        while low <= high:
            middle = (low + high) // 2
            _, insertion_timestamp = value_and_timestamps[middle]
            if insertion_timestamp > timestamp:
                high = middle - 1
            else:
                low = middle + 1

        latest_leq_timestamp = low - 1
        if latest_leq_timestamp == -1:
            return ""
        return value_and_timestamps[latest_leq_timestamp][0]
