# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, idx):
            if not node:
                return
            if len(ans) <= idx:
                ans.append(node.val)
            else:
                ans[idx] = max(ans[idx], node.val)
            dfs(node.left, idx+1)
            dfs(node.right, idx+1)
        dfs(root, 0)
        return ans
