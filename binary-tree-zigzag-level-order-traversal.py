# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return
            if level == len(ans):
                ans.append(deque())
            if level % 2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].appendleft(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        ans = []
        helper(root, 0)
        return ans
