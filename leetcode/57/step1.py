class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        intervals_after_insertion: list[int] = []
        insertion_start, insertion_end = newInterval
        is_inserted = False
        for start, end in intervals:
            if end < insertion_start:
                intervals_after_insertion.append([start, end])
                continue

            if insertion_end < start:
                if not is_inserted:
                    intervals_after_insertion.append([insertion_start, insertion_end])
                    is_inserted = True
                intervals_after_insertion.append([start, end])
                continue

            insertion_start = min(start, insertion_start)
            insertion_end = max(end, insertion_end)

        if not is_inserted:
            intervals_after_insertion.append([insertion_start, insertion_end])
        return intervals_after_insertion
