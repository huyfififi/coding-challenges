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
        jobs = []
        for i in range(len(startTime)):
            jobs.append(Job(start=startTime[i], end=endTime[i], profit=profit[i]))
        jobs.sort(key=lambda job: job.start)

        max_profit = [0] * (len(jobs) + 1)  # max_profit[i] -> max with jobs[i:]
        for i in range(len(jobs) - 1, -1, -1):
            job = jobs[i]
            non_overlapping = bisect.bisect_left(
                jobs, job.end, lo=i + 1, key=lambda x: x.start
            )
            if non_overlapping == i:  # in hindsight, this is redundant
                max_profit[i] = max_profit[i + 1]
                continue

            max_profit[i] = max(
                max_profit[i + 1], job.profit + max_profit[non_overlapping]
            )

        return max_profit[0]
