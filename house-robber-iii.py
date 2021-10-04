# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob, norob = {}, {}
        def helper(node, robParent):
            if not node:
                return 0
            if robParent:
                if node in norob:
                    return norob[node]
                norob[node] = helper(node.left, False)+helper(node.right, False)
                return norob[node]
            else:
                if node in rob:
                    return rob[node]
                rob[node] = max(node.val+helper(node.left,True)+helper(node.right,True), helper(node.left,False)+helper(node.right,False))
                return rob[node]
        return helper(root, False)
