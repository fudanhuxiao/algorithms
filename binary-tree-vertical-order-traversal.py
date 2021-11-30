# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        queue = deque([[root, 0]])
        while queue:
            node, i = queue.popleft()
            ans[i].append(node.val)
            if node.left:
                queue.append([node.left, i-1])
            if node.right:
                queue.append([node.right, i+1])
        low, high = min(ans.keys()), max(ans.keys())
        ret = []
        for i in range(low, high+1):
            ret.append(ans[i])
        return ret
            
            
