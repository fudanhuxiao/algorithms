class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        minheap = [(0, 0, 0)]
        dist = {}
        while minheap:
            cost, i, j = heappop(minheap)
            dist[(i, j)] = cost
            if i == m-1 and j == n-1:
                return dist[(i, j)]
            for k in range(4):
                x, y = i+dirs[k][0], j+dirs[k][1]
                if k == grid[i][j]-1:
                    weight = 0
                else:
                    weight = 1
                if x >= 0 and y >= 0 and x < m and y < n and ((x, y) not in dist or cost+weight<dist[(x, y)]):
                    dist[(x, y)] = cost+weight
                    heappush(minheap, (cost+weight, x, y))
                
                
