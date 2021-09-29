# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return float('inf'), float('-inf'), 0
            llow, lhigh, lcount = dfs(node.left)
            rlow, rhigh, rcount = dfs(node.right)
            if lhigh < node.val and rlow > node.val:
                count = lcount+rcount+1
                if count > self.count:
                    self.count = count
                return min(node.val, llow), max(node.val, rhigh), count
            return float('-inf'), float('inf'), 0
        dfs(root)
        return self.count
            
            
            
