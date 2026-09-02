class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for n in range(n+1):
            count = 0
            for i in range(32):          
                if (1 << i) & n:
                    count+=1
            output.append(count)
        return output