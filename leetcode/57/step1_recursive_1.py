class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        insert_start, insert_end = newInterval
        head_start, head_end = intervals[0]
        if head_end < insert_start:
            return [intervals[0]] + self.insert(intervals[1:], newInterval)
        if insert_end < head_start:
            return [newInterval] + intervals
        return self.insert(
            intervals[1:], [min(insert_start, head_start), max(insert_end, head_end)]
        )
