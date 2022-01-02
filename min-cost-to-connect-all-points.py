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
    
    def connected(self, x, y):
        return self.find(y) == self.find(x)

class Kruskal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap, n, uf = [], len(points), UnionFind()
        for i in range(n-1):
            uf.add(i)
            for j in range(i+1, n):
                uf.add(j)
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heappush(minheap, (dist, i, j))
        ans = 0
        while minheap and n > 1:
            dist, i, j = heappop(minheap)
            if not uf.connected(i, j):
                uf.union(i, j)
                ans += dist
                n -= 1
        return ans



class Prim:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap, n, visited = [], len(points), set([0])
        for i in range(1, n):
            dist = abs(points[0][0]-points[i][0])+abs(points[0][1]-points[i][1])
            heappush(minheap, [dist, i])
        ans = 0
        while len(visited) < n:
            dist, i = heappop(minheap)
            if i not in visited:
                visited.add(i)
                ans += dist
                for j in range(1, n):
                    if j not in visited:
                        d = abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1])
                        heappush(minheap, [d, j])
        return ans
