import math


class MedianFinder:
    # numbers are in this range [-100000, 100000]
    OFFSET = 10**5
    NUM_VALUES = 2 * OFFSET + 1
    VALUES_PER_BUCKET = math.isqrt(NUM_VALUES)
    NUM_BUCKETS = NUM_VALUES // VALUES_PER_BUCKET + 1

    def __init__(self):
        self.value_count = [0] * self.NUM_VALUES
        self.bucket_count = [0] * self.NUM_BUCKETS
        self.num_count = 0

    def addNum(self, num: int) -> None:
        num += self.OFFSET
        self.value_count[num] += 1
        self.bucket_count[num // self.VALUES_PER_BUCKET] += 1
        self.num_count += 1

    def findMedian(self) -> float:
        low = self.find_kth((self.num_count - 1) // 2)
        high = self.find_kth(self.num_count // 2)
        return (low + high) / 2

    def find_kth(self, k: int) -> int:
        bucket_index = 0
        while k >= self.bucket_count[bucket_index]:
            k -= self.bucket_count[bucket_index]
            bucket_index += 1

        num = bucket_index * self.VALUES_PER_BUCKET
        while k >= self.value_count[num]:
            k -= self.value_count[num]
            num += 1

        return num - self.OFFSET
