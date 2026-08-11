import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        label_to_count = collections.Counter(tasks)

        max_count = max(label_to_count.values())

        num_most_frequent_labels = 0
        for count in label_to_count.values():
            if count == max_count:
                num_most_frequent_labels += 1

        num_gaps = max_count - 1
        empty_slots_per_gap = max(0, n - (num_most_frequent_labels - 1))
        empty_slots = num_gaps * empty_slots_per_gap

        num_infrequent_tasks = len(tasks) - max_count * num_most_frequent_labels

        num_unfilled_slots = max(0, empty_slots - num_infrequent_tasks)
        return len(tasks) + num_unfilled_slots
