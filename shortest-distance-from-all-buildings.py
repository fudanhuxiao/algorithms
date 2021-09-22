class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reachable = [[0]*n for _ in range(m)]
        distance = [[0]*n for _ in range(m)]
        numBuildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numBuildings += 1
                    if not self.bfs(grid, i, j, reachable, distance):
                        return -1
        minDist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reachable[i][j] == numBuildings and distance[i][j] < minDist:
                    minDist = distance[i][j]
        return minDist if minDist < float('inf') else -1
        
                    
    def bfs(self, grid, x, y, reachable, distance):
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        visited = [[False]*n for _ in range(m)]
        d = 0
        queue.append([x,y])
        visited[x][y] == True
        while queue:
            size = len(queue)
            d += 1
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    r, c = i+di, j+dj
                    if r >= 0 and c >= 0 and r < m and c < n and grid[r][c] != 2 and not visited[r][c]:
                        if grid[r][c] == 0:
                            reachable[r][c] += 1
                            distance[r][c] += d
                            queue.append([r,c])
                        visited[r][c] = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    return False
        return True
            
                
