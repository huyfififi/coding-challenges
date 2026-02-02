import collections


class TimeMap:
    def __init__(self):
        self.key_to_value_and_timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_and_timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_and_timestamps = self.key_to_value_and_timestamps[key]

        low = 0  # i < low: value_and_timestamps[i][1] <= timestamp
        high = len(
            value_and_timestamps
        )  # high <= i: value_and_timestamps[i][1] > timestamp
        while low < high:
            middle = (low + high) // 2
            if value_and_timestamps[middle][1] > timestamp:
                high = middle
            else:
                low = middle + 1

        latest_leq_timestamp = low - 1
        if latest_leq_timestamp == -1:
            return ""
        return value_and_timestamps[latest_leq_timestamp][0]
