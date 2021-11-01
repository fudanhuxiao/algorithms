# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        h = 0
        cur = root
        while cur:
            cur = cur.left
            h += 1
        if h <= 1:
            return h
        h -= 1
        
        def existed(idx, h, node):
            start, end = 1, 2**h
            for _ in range(h):
                mid = (start+end)//2
                if idx <= mid:
                    node = node.left
                    end = mid
                else:
                    node = node.right
                    start = mid
            return node is not None
        
        start, end = 1, 2**h
        while start + 1 < end:
            mid = (start+end)//2
            if existed(mid, h, root):
                start = mid
            else:
                end = mid-1
        return 2**h-1+end if existed(end, h, root) else 2**h-1+start
