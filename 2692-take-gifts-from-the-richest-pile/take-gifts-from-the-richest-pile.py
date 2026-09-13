class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = [-g for g in gifts]
        heapq.heapify(maxheap)
        for _ in range(k):
            n = -heapq.heappop(maxheap)
            heapq.heappush(maxheap, -math.isqrt(n))
        return -sum(maxheap)