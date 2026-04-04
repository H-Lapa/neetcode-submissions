class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-stone for stone in stones]
        heapq.heapify(stoneHeap)
        print(stoneHeap)
        while len(stoneHeap) > 1:
            x = heapq.heappop(stoneHeap)
            y = heapq.heappop(stoneHeap)

            if x != y:
                heapq.heappush(stoneHeap, x-y)

        if not stoneHeap:
            return 0

        return -stoneHeap[0]