# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return -1    
        level_sums = []        
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return        
            if depth == len(level_sums):
                level_sums.append(0)
            level_sums[depth] += node.val        
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)         
        dfs(root, 0)        
        if len(level_sums) < k:
            return -1            
        level_sums.sort(reverse=True)
        return level_sums[k - 1]
            