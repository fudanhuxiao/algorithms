"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ls = []
        self.rserialize(root, ls)
        return ','.join(ls)
    
    def rserialize(self, root, ls):
        if not root:
            return
        ls.append(str(root.val))
        ls.append(str(len(root.children)))
        for node in root.children:
            self.rserialize(node, ls)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        queue = deque(data.split(','))
        return self.rdeserialize(queue)
    
    def rdeserialize(self, queue):
        root = Node(int(queue.popleft()), [])
        size = int(queue.popleft())
        for _ in range(size):
            root.children.append(self.rdeserialize(queue))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
