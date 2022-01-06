class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        while queue:
            x, y, remain, steps = queue.popleft()
            if x == m-1 and y == n-1:
                return steps
            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                i, j = x+di, y+dj
                if i >= 0 and j >= 0 and i < m and j < n:
                    if grid[i][j] == 0 and (i, j, remain) not in visited:
                        visited.add((i, j, remain))
                        queue.append((i, j, remain, steps+1))
                    elif grid[i][j] == 1 and remain > 0 and (i, j, remain-1) not in visited:
                        visited.add((i, j, remain-1))
                        queue.append((i, j, remain-1, steps+1))
        return -1
