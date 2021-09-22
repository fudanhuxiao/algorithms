class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        areas = []
        color = 1
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    color += 1
                    areas.append(self.dfs(grid, i, j, color))
        if len(areas) <= 0:
            return 1
        if areas[0] == n*n:
            return areas[0]
        maxarea = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    colors = set()
                    area = 1
                    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                        x, y = i+di, j+dj
                        if x >= 0 and y >= 0 and x < n and y < n and grid[x][y] > 1 and grid[x][y] not in colors:
                            colors.add(grid[x][y])
                            area += areas[grid[x][y]-2]
                    maxarea = max(maxarea, area)
        return maxarea
                            
                            
    
    def dfs(self, grid, i, j, color):
        if i >= len(grid) or j >= len(grid) or i < 0 or j < 0 or grid[i][j] != 1:
            return 0
        grid[i][j] = color
        return 1 + self.dfs(grid, i+1, j, color)+self.dfs(grid, i-1, j, color)+self.dfs(grid, i, j+1, color)+self.dfs(grid, i, j-1, color)
    
