from collections import deque
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'T':
                    target = (i,j)
                elif grid[i][j] == 'B':
                    box = (i,j)
                elif grid[i][j] == 'S':
                    person = (i,j)
                    
        def valid(place):
            return place[0]>=0 and place[0]<len(grid) and place[1]>=0 and place[1]<len(grid[0]) and grid[place[0]][place[1]] != '#'
        
        def reachable(start, end):
            q, v = deque(), set()
            q.append(start)
            v.add(start)
            while q:
                i,j = q.popleft()
                if (i,j) == end:
                    return True
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if valid((ni, nj)) and (ni,nj) not in v and (ni, nj) != box:
                        q.append((ni,nj))
                        v.add((ni,nj))
            return False
        
        queue, visited = deque(), set()
        queue.append((0,box,person))
        visited.add(box+person)
        while queue:
            dist, box, person = queue.popleft()
            if box == target:
                return dist
            newbox, newperson = [], []
            for di, dj in dirs:
                newbox.append((box[0]+di, box[1]+dj))
                newperson.append((box[0]-di, box[1]-dj))
            for i in range(4):
                if valid(newperson[i]) and valid(newbox[i]) and reachable(person, newperson[i]) and (newbox[i]+box) not in visited:
                    queue.append((dist+1, newbox[i], box))
                    visited.add(newbox[i]+box)
        return -1
                    
