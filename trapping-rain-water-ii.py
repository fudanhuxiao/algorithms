class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        minheap = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            heappush(minheap, (heightMap[i][0], i, 0))
            heappush(minheap, (heightMap[i][n-1], i, n-1))
            visited[i][0], visited[i][n-1] = True, True
        for j in range(1, n-1):
            heappush(minheap, (heightMap[0][j], 0, j))
            heappush(minheap, (heightMap[m-1][j], m-1, j))
            visited[0][j], visited[m-1][j] = True, True
        ans = 0
        while minheap:
            minwater, x, y = heappop(minheap)
            for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                nx, ny = x+dx, y+dy
                if nx >= 0 and ny >= 0 and nx < m and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(minwater-heightMap[nx][ny], 0)
                    heappush(minheap, (max(heightMap[nx][ny], minwater), nx, ny))
        return ans
