class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        intervals_after_insertion: list[int] = []

        def insert_helper(i: int, interval_to_insert: list[int]) -> None:
            if i == len(intervals):
                if interval_to_insert:
                    intervals_after_insertion.append(interval_to_insert)
                return

            interval = intervals[i]
            if not interval_to_insert:
                intervals_after_insertion.append(interval)
                insert_helper(i + 1, interval_to_insert)
                return

            interval_start, interval_end = interval
            interval_to_insert_start, interval_to_insert_end = interval_to_insert
            if interval_end < interval_to_insert_start:
                intervals_after_insertion.append(interval)
                insert_helper(i + 1, interval_to_insert)
                return

            if interval_to_insert_end < interval_start:
                intervals_after_insertion.append(interval_to_insert)
                insert_helper(i, [])
                return

            merged_interval = [
                min(interval_start, interval_to_insert_start),
                max(interval_end, interval_to_insert_end),
            ]
            insert_helper(i + 1, merged_interval)

        insert_helper(0, newInterval)
        return intervals_after_insertion
