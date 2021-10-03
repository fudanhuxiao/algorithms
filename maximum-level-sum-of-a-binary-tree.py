# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        level = 0
        maxsum, maxlevel = root.val, 1
        while queue:
            level += 1
            size = len(queue)
            lsum = 0
            for _ in range(size):
                cur = queue.popleft()
                lsum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if lsum > maxsum:
                maxsum = lsum
                maxlevel = level
        return maxlevel
