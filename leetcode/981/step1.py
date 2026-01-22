import bisect
import collections


class TimeMap:
    def __init__(self):
        self.key_to_value_and_timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_and_timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_and_timestamps = self.key_to_value_and_timestamps[key]
        # index of ["", *value_and_timestamps]
        return_index = bisect.bisect_right(
            value_and_timestamps, timestamp, key=lambda x: x[1]
        )
        if return_index == 0:
            return ""
        return value_and_timestamps[return_index - 1][0]
