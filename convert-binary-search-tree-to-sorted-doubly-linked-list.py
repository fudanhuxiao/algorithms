"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        def helper(root):
            if not root:
                return None, None
            head, tail = root, root
            if root.left:
                left_head, left_tail = helper(root.left)
                left_tail.right = root
                root.left = left_tail
                head = left_head
            if root.right:
                right_head, right_tail = helper(root.right)
                root.right = right_head
                right_head.left = root
                tail = right_tail
            return head, tail
        head, tail = helper(root)
        head.left = tail
        tail.right = head
        return head
