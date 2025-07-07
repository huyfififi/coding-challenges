class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        num_intervals = len(intervals)
        new_intervals: list[list[int]] = []
        insertion_start, insertion_end = newInterval

        i = 0
        while i < num_intervals and intervals[i][1] < insertion_start:
            new_intervals.append(intervals[i])
            i += 1

        while i < num_intervals and intervals[i][0] <= insertion_end:
            insertion_start = min(insertion_start, intervals[i][0])
            insertion_end = max(insertion_end, intervals[i][1])
            i += 1

        new_intervals.append([insertion_start, insertion_end])
        new_intervals.extend(intervals[i:])
        return new_intervals
