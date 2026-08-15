class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1 , max(piles)
        output = 0
        while l <= r:
            k=(l+r)//2

            totalhours = 0
            for p in piles:
                totalhours += math.ceil(float(p)/k)
            if totalhours <= h:
                output = k
                r = k - 1
            else:
                l= k + 1
        return output