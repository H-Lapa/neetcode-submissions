class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums) # num: freq
        heap = []
        heapq.heapify(heap)

        for key in numCount.keys():
            x = (numCount[key], key)
            heapq.heappush(heap, x)

            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]

        