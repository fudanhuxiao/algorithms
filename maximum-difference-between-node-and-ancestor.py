# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.v = 0
        self.helper(root.val, root.val, root)
        return self.v
        
    def helper(self, rootmax, rootmin, cur):
        if not cur:
            return
        self.v = max(self.v, abs(rootmax-cur.val), abs(rootmin-cur.val))
        rootmax = max(rootmax, cur.val)
        rootmin = min(rootmin, cur.val)
        self.helper(rootmax, rootmin, cur.left)
        self.helper(rootmax, rootmin, cur.right)
