class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        for val in pushed:
            stack.append(val)
            while stack and (stack[-1] == popped[j]):
                i -= 1
                j +=1
                stack.pop()
            i+=1
        return i == 0