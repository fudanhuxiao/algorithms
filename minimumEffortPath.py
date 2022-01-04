class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minheap, dist, effort = [(0, 0, 0)], {}, 0 
        while minheap:
            d, x, y = heappop(minheap)
            effort = max(effort, d)
            if x == len(heights)-1 and y == len(heights[0])-1:
                return effort
            if (x, y) not in dist:
                dist[(x, y)] = d
                for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    i,j = x+di, y+dj
                    if i >= 0 and j >= 0 and i < len(heights) and j < len(heights[0]) and (i, j) not in dist:
                        d2 = abs(heights[x][y]-heights[i][j])
                        heappush(minheap, (d2, i, j))
