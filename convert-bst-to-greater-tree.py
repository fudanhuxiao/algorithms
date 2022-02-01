# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def helper(root):
            if not root:
                return
            helper(root.right)
            self.total += root.val
            root.val = self.total
            helper(root.left)
        helper(root)
        return root
