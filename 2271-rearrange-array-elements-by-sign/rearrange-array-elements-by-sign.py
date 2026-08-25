class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        pos , neg = 0, 1
        
        for i in range(len(nums)):
            if nums[i]< 0:
                result[neg] = nums[i]
                neg+=2
            else:
                result[pos] = nums[i]
                pos += 2
        return result