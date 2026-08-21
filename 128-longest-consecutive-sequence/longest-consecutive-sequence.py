class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        max_count=0
        for i in hs:
            if i-1 not in hs:
                count =1
                while (i+count) in hs:
                    count +=1
                max_count = max(count,max_count)
        return max_count