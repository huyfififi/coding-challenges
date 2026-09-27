import math


class MedianFinder:
    OFFSET = 10**5
    NUM_VALUES = 2 * OFFSET + 1
    VALUES_PER_CHUNK = math.isqrt(NUM_VALUES)
    NUM_CHUNKS = NUM_VALUES // VALUES_PER_CHUNK + 1

    def __init__(self):
        self.value_counts = [0] * self.NUM_VALUES
        self.chunk_counts = [0] * self.NUM_CHUNKS
        self.num_count = 0

    def addNum(self, num: int) -> None:
        self.num_count += 1
        shifted = num + self.OFFSET
        self.value_counts[shifted] += 1
        self.chunk_counts[shifted // self.VALUES_PER_CHUNK] += 1

    def findMedian(self) -> float:
        lo = self.find_kth((self.num_count - 1) // 2)
        hi = self.find_kth(self.num_count // 2)
        return (lo + hi) / 2

    def find_kth(self, k: int) -> int:
        chunk = 0
        while self.chunk_counts[chunk] <= k:
            k -= self.chunk_counts[chunk]
            chunk += 1

        shifted = chunk * self.VALUES_PER_CHUNK
        while self.value_counts[shifted] <= k:
            k -= self.value_counts[shifted]
            shifted += 1

        return shifted - self.OFFSET
