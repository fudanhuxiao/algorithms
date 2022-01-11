# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = self.getSum(root)
        self.best = 0
        self.dfs(root)
        return self.best*(self.total-self.best)%(10**9+7)
    
    def getSum(self, root):
        if not root:
            return 0
        return root.val + self.getSum(root.left) + self.getSum(root.right)
    
    def dfs(self, root):
        if not root:
            return 0
        cur = root.val + self.dfs(root.left) + self.dfs(root.right)
        if abs(cur-self.total/2) < abs(self.best-self.total/2):
            self.best = cur
        return cur
