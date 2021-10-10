# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.lastlevel = deque()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.lastlevel.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        node = self.lastlevel[0]
        self.lastlevel.append(TreeNode(val))
        if not node.left:
            node.left = self.lastlevel[-1]
        else:
            node.right = self.lastlevel[-1]
            self.lastlevel.popleft()
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
