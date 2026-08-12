import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        label_to_count = collections.Counter(tasks)

        max_frequency = max(label_to_count.values())

        num_most_frequent_labels = 0
        for count in label_to_count.values():
            if count == max_frequency:
                num_most_frequent_labels += 1

        num_gaps = max_frequency - 1
        empty_slots_per_gap = max(0, n - (num_most_frequent_labels - 1))
        num_empty_slots = num_gaps * empty_slots_per_gap

        num_other_tasks = len(tasks) - max_frequency * num_most_frequent_labels

        return len(tasks) + max(0, num_empty_slots - num_other_tasks)
