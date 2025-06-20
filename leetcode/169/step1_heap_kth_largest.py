import heapq


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_threshold = len(nums) // 2 + 1
        min_heap = []

        for num in nums:
            if len(min_heap) < majority_threshold:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return heapq.heappop(min_heap)
