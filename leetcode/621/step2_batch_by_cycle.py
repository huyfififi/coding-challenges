import collections
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        label_to_count = collections.Counter(tasks)
        negated_counts = []
        for count in label_to_count.values():
            negated_counts.append(-count)

        heapq.heapify(negated_counts)

        time = 0
        cycle_length = n + 1

        while negated_counts:
            num_tasks_done = min(cycle_length, len(negated_counts))
            next_counts = []

            for _ in range(num_tasks_done):
                count = -heapq.heappop(negated_counts)
                if count > 1:
                    next_counts.append(count - 1)

            for count in next_counts:
                heapq.heappush(negated_counts, -count)

            if negated_counts:
                time += cycle_length
            else:
                time += num_tasks_done

        return timeimport collections
