import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        label_to_count = collections.defaultdict(int)
        for label in tasks:
            label_to_count[label] += 1

        label_to_cool_time = collections.defaultdict(int)
        remaining_labels = set(label_to_count)

        intervals = 0
        while len(remaining_labels) > 0:
            available_label_to_count = {
                label: count
                for label, count in label_to_count.items()
                if label_to_cool_time[label] == 0 and label in remaining_labels
            }
            if most_frequent_label := max(
                available_label_to_count, key=available_label_to_count.get, default=None
            ):
                label_to_count[most_frequent_label] -= 1
                if label_to_count[most_frequent_label] == 0:
                    remaining_labels.remove(most_frequent_label)
                else:
                    label_to_cool_time[most_frequent_label] = n + 1

            for label in label_to_cool_time:
                if label_to_cool_time[label] == 0:
                    continue

                label_to_cool_time[label] -= 1

            intervals += 1

        return intervals
