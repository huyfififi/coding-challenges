import collections
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        label_to_count = collections.defaultdict(int)
        for label in tasks:
            label_to_count[label] += 1

        negated_counts_heap = []
        for count in label_to_count.values():
            heapq.heappush(negated_counts_heap, -count)

        del label_to_count

        time = 0
        cycle_length = n + 1
        while negated_counts_heap:
            time_in_cycle = 0
            num_tasks_done = 0
            next_counts = []

            while time_in_cycle < cycle_length and negated_counts_heap:
                count = -heapq.heappop(negated_counts_heap)
                num_tasks_done += 1
                if count > 1:
                    next_counts.append(count - 1)

                time_in_cycle += 1

            for count in next_counts:
                heapq.heappush(negated_counts_heap, -count)

            if negated_counts_heap:
                time += cycle_length
            else:
                time += num_tasks_done

        return time
