import bisect
import dataclasses


@dataclasses.dataclass
class Job:
    start: int
    end: int
    profit: int


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        jobs = [
            Job(start, end, profit)
            for start, end, profit in zip(startTime, endTime, profit)
        ]
        jobs.sort(key=lambda job: job.start)

        # max_profit[i] = maximum profit obtainable from jobs[i:]
        max_profit = [0] * (len(jobs) + 1)

        for i in range(len(jobs) - 1, -1, -1):
            job = jobs[i]
            next_compatible = bisect.bisect_left(
                jobs, job.end, lo=i + 1, key=lambda x: x.start
            )

            max_profit[i] = max(
                max_profit[i + 1],
                job.profit + max_profit[next_compatible],
            )

        return max_profit[0]
