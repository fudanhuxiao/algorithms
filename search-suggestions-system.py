class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = -1

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for i in range(len(products)):
            node = root
            for p in products[i]:
                j = ord(p)-ord('a')
                if not node.children[j]:
                    node.children[j] = TrieNode()
                node = node.children[j]
            node.isWord = i
        ans = []
        node = root
        
        def dfs(root, buffer):
            if not root or len(buffer) >= 3:
                return
            if root.isWord != -1:
                buffer.append(products[root.isWord])
            for k in range(26):
                dfs(root.children[k], buffer)
        
        for c in searchWord:
            buffer = []
            if node is not None:
                node = node.children[ord(c)-ord('a')]
                dfs(node, buffer)
            ans.append(buffer)
        return ans
    
    
            
        
            
        
