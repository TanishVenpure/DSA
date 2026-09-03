class Solution:
    def reverse(self, x: int) -> int:
        min_int, max_int = -2**31, 2**31 - 1     
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            rev = rev * 10 + (x % 10)
            x //= 10      
        rev *= sign
        if rev < min_int or rev > max_int:
            return 0     
        return rev