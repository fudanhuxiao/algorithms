class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.maxgold = 0
        visited = [[False]*n for _ in range(m)]
        def dfs(x, y, gold):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0 or visited[x][y]:
                return 
            visited[x][y] = True
            gold += grid[x][y]
            self.maxgold = max(self.maxgold, gold)
            dfs(x+1, y, gold)
            dfs(x-1, y, gold)
            dfs(x, y+1, gold)
            dfs(x, y-1, gold)
            visited[x][y] = False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return self.maxgold
                    
