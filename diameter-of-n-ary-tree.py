"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        def depth(node, curDepth):
            if not node.children:
                return curDepth
            top1, top2 = curDepth, curDepth
            for child in node.children:
                maxdepth = depth(child, curDepth+1)
                if maxdepth > top1:
                    top1, top2 = maxdepth, top1
                elif maxdepth > top2:
                    top2 = maxdepth
            self.ans = max(self.ans, top1+top2-2*curDepth)
            return top1
        depth(root, 0)
        return self.ans
            
