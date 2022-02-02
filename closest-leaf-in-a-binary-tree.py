# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        self.graph = {}
        self.target = None
        self.buildGraph(root, None, k)
        queue = deque([self.target])
        visited = set([self.target])
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                return node.val
            dirs = [node.left, node.right]
            if node in self.graph:
                dirs.append(self.graph[node])
            for child in dirs:
                if child and child not in visited:
                    visited.add(child)
                    queue.append(child)
                    
    def buildGraph(self, child, parent, k):
        if not child or self.target:
            return
        self.graph[child] = parent
        if child.val == k:
            self.target = child
            return
        self.buildGraph(child.left, child, k)
        self.buildGraph(child.right, child, k)
