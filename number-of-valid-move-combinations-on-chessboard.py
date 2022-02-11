class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        dirs = {'rook':[(0,1),(1,0),(0,-1),(-1,0)],'bishop':[(1,1),(1,-1),(-1,1),(-1,-1)],'queen':[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]}
        n = len(pieces)
        directions = [[]]
        for i in range(n):
            level = []
            for d in dirs[pieces[i]]:
                for prev in directions:
                    new = list(prev)
                    new.append(d)
                    level.append(new)
            directions = level
        self.visited = set()
        positions = [[x-1, y-1, True] for x, y, in positions]
        for direction in directions:
            self.dfs(direction, positions)
        return len(self.visited)
            
    def dfs(self, direction, position):
        stack = [[]]
        n = len(direction)
        for i in range(n):
            level = []
            if position[i][2]:
                pos = [position[i][0]+direction[i][0], position[i][1]+direction[i][1], True]
                for prev in stack:
                    new = list(prev)
                    new.append(pos)
                    level.append(new)
            pos = [position[i][0], position[i][1], False]
            for prev in stack:
                new = list(prev)
                new.append(pos)
                level.append(new)
            stack = level
        for pos in stack:
            valid = self.isValid(pos)
            if valid:
                encode = self.hash(pos)
                if encode not in self.visited:
                    self.visited.add(encode)
                    self.dfs(direction, pos)
    
    def isValid(self, position):
        s = set()
        for x, y, state in position:
            if x < 0 or y < 0 or x >= 8 or y >= 8 or (x, y) in s:
                return False
            s.add((x, y))
        return True
    
    def hash(self, position):
        ans = []
        for i in range(len(position)):
            x, y, state = position[i]
            ans.append(x*8+y)
        return tuple(ans)
