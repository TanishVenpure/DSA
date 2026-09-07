class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if y != x:
                heapq.heappush(maxheap , -(x-y))
        return -maxheap[0] if maxheap else 0