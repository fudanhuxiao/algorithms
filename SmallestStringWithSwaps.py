class UnionFind:
    def __init__(self):
        self.father = {}
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            self.father[rootx] = rooty
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        while x != root:
            og_father = self.father[x]
            self.father[x] = root
            x = og_father
        return root

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf, n = UnionFind(), len(s)
        for i in range(n):
            uf.add(i)
        for a, b in pairs:
            uf.union(a, b)
        pq = {}
        for i in range(n):
            root = uf.find(i)
            if root not in pq:
                pq[root] = []
            heappush(pq[root], s[i])
        ans = []
        for i in range(n):
            root = uf.find(i)
            ans.append(heappop(pq[root]))
        return ''.join(ans)
