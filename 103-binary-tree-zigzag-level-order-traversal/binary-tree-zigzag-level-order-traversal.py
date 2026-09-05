# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        q = deque([root])
        flag = True
        while q:
            size = len(q)
            level = [0]*size
            for i in range(size):
                node = q.popleft()
                index = i if flag else size - i - 1
                level[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            flag = not flag
            res.append(level)
        return res