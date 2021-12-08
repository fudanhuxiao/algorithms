class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees, m, n = [], len(forest), len(forest[0])
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append([forest[r][c], r, c])
        trees.sort()
        prev = (0, 0)
        steps = 0
        for i in range(len(trees)):
            val, r, c = trees[i]
            dist = self.distance(prev, r, c, forest)
            if dist == -1:
                return -1
            steps += dist
            prev = (r,c)
        return steps
    
    def distance(self, frm, r, c, forest):
        queue = deque([frm])
        visited = set([frm])
        dist = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                i, j = queue.popleft()
                if i == r and j == c:
                    return dist
                for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
                    ni, nj = i+di, j+dj
                    if ni >= 0 and ni < len(forest) and nj >= 0 and nj < len(forest[0]) and forest[i][j] > 0 and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        queue.append((ni, nj))
            dist += 1
        return -1
                        
