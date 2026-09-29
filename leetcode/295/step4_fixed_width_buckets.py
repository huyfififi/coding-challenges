class MedianFinder:
    """
    Same structure as sqrt decomposition, but with a hand-picked bucket width (100).
    """

    OFFSET = 10**5
    NUM_VALUES = OFFSET * 2 + 1
    # any size near sqrt (NUM_VALUES) ~= 447 should work
    # VALUES_PER_BUCKET = 10 ** 4  # TLE
    VALUES_PER_BUCKET = 10**3
    # VALUES_PER_BUCKET = 10 ** 2  # AC
    # VALUES_PER_BUCKET = 10 ** 1  # TLE
    NUM_BUCKETS = NUM_VALUES // VALUES_PER_BUCKET + 1

    def __init__(self):
        self.counts = [0] * self.NUM_VALUES
        self.buckets = [0] * self.NUM_BUCKETS
        self.num_count = 0

    def addNum(self, num: int) -> None:
        self.num_count += 1
        shifted_num = num + self.OFFSET
        self.counts[shifted_num] += 1
        self.buckets[shifted_num // self.VALUES_PER_BUCKET] += 1

    def findMedian(self) -> float:
        low = self.find_kth((self.num_count - 1) // 2)
        high = self.find_kth(self.num_count // 2)
        return (low + high) / 2

    def find_kth(self, k: int) -> int:
        bucket = 0
        while self.buckets[bucket] <= k:
            k -= self.buckets[bucket]
            bucket += 1

        shifted_num = bucket * self.VALUES_PER_BUCKET
        while self.counts[shifted_num] <= k:
            k -= self.counts[shifted_num]
            shifted_num += 1

        return shifted_num - self.OFFSET
