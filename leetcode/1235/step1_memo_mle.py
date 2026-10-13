import collections
import functools


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        end_to_indices = collections.defaultdict(list)
        last_end = max(endTime)
        for i, end in enumerate(endTime):
            end_to_indices[end].append(i)

        @functools.cache
        def max_profit(time: int) -> int:
            if time == 0:
                return 0

            max_ = float("-inf")
            for i in end_to_indices[time]:
                max_ = max(max_, max_profit(startTime[i]) + profit[i])

            max_ = max(max_, max_profit(time - 1))
            return max_

        return max_profit(last_end)
