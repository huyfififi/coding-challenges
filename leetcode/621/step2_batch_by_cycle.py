import collections
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        label_to_count = collections.Counter(tasks)
        negated_counts = []
        for count in label_to_count.values():
            negated_counts.append(-count)

        heapq.heapify(negated_counts)

        intervals = 0
        batch_size = n + 1
        while negated_counts:
            next_counts = []

            num_tasks_done = min(batch_size, len(negated_counts))
            for _ in range(num_tasks_done):
                count = -heapq.heappop(negated_counts)
                if count > 1:
                    next_counts.append(count - 1)

            for count in next_counts:
                heapq.heappush(negated_counts, -count)

            if negated_counts:
                intervals += batch_size
            else:
                intervals += num_tasks_done

        return intervals
