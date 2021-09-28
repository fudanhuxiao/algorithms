class Trie:
    def __init__(self):
        self.children = {}
        self.index = -1

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for i in range(len(folder)):
            names = folder[i].split('/')
            cur = root
            for c in names[1:]:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.index = i
        ans = []
        def dfs(node):
            if node.index != -1:
                ans.append(folder[node.index])
                return
            for c in node.children:
                dfs(node.children[c])
        dfs(root)
        return ans
            
            
