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
            next_counts = []
            num_tasks_done = 0

            for _ in range(min(cycle_length, len(negated_counts_heap))):
                count = -heapq.heappop(negated_counts_heap)
                if count > 1:
                    next_counts.append(count - 1)
                num_tasks_done += 1

            for count in next_counts:
                heapq.heappush(negated_counts_heap, -count)

            if negated_counts_heap:
                time += cycle_length
            else:
                time += num_tasks_done

        return time
