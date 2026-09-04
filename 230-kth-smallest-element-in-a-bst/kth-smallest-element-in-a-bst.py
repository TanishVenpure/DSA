# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(root):
            if not root or len(arr) == k:
                return 
            inorder(root.left)
            if len(arr) < k:
                arr.append(root.val)
            inorder(root.right)
        inorder(root)
        return arr[-1]