class UnionFind:
    def __init__(self):
        self.father = {}
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if rootx == 0 or rooty == 0:
                self.father[rootx], self.father[rooty] = 0, 0
            else:
                self.father[rootx] = rooty
            
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        schedules = defaultdict(list)
        for x, y, time in meetings:
            schedules[time].append([x,y])
        orders = sorted(schedules.keys())
        uf = UnionFind()
        for i in range(n):
            uf.add(i)
        uf.union(0, firstPerson)
        for time in orders:
            for x, y in schedules[time]:
                uf.union(x, y)
            for x, y in schedules[time]:
                rootx = uf.find(x)
                if rootx != 0:
                    uf.father[x] = x
                    uf.father[y] = y
        ans = []
        for x in range(n):
            if uf.find(x) == 0:
                ans.append(x)
        return ans
            
            
                
            
