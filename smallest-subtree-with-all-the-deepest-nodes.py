# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None, 0
            lnode, ldist = dfs(node.left)
            rnode, rdist = dfs(node.right)
            if ldist > rdist:
                return lnode, ldist+1
            elif rdist > ldist:
                return rnode, rdist+1
            return node, ldist+1
        return dfs(root)[0]
