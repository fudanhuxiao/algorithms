# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append(root)
        findNone = False
        while queue:
            cur = queue.popleft()
            if not cur:
                findNone = True
            else:
                if findNone:
                    return False
                queue.append(cur.left)
                queue.append(cur.right)
        return True
                    
                
                
