class UnionFind:
    def __init__(self):
        self.father = {}
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
    
    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        self.father[roota] = rootb
        
    def find(self, x):
        rootx = x
        while self.father[rootx]:
            rootx = self.father[rootx]
        while x != rootx:
            ori_father = self.father[x]
            self.father[x] = rootx
            x = ori_father
        return rootx
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for x, e, _, y in equations:
            uf.add(x)
            uf.add(y)
            if e == '=' and (x != y and not uf.connected(x, y)):
                uf.union(x, y)
        for x, e, _, y in equations:
            if e == '!' and (x == y or uf.connected(x, y)):
                return False
        return True
                    
