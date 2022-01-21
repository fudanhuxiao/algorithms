# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ans = deque()
        def inorder(ans, node):
            if not node:
                return
            inorder(ans, node.left)
            if len(ans) < k:
                ans.append(node.val)
            else:
                if abs(node.val-target) < abs(ans[0]-target):
                    ans.popleft()
                    ans.append(node.val)
                else:
                    return
            inorder(ans, node.right)
        inorder(ans, root)
        return ans
