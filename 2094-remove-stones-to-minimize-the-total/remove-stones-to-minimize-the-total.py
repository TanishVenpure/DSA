class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap = [-p for p in piles]
        heapq.heapify(maxheap)
        for _ in range (k):
            largest = -heapq.heappop(maxheap)
            remaining = largest - (largest // 2)
            heapq.heappush(maxheap, -remaining)
        return -sum(maxheap)