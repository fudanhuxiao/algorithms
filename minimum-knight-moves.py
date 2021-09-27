class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = [[None]*(abs(y)+3) for _ in range(abs(x)+3)]
        def dfs(x, y):
            if x+y == 0:
                memo[x][y] = 0
                return 0
            if x+y == 2:
                memo[x][y] = 2
                return 2
            if memo[x][y]:
                return memo[x][y]
            else:
                memo[x][y] = 1+min(dfs(abs(x-1),abs(y-2)),dfs(abs(x-2),abs(y-1)))
            return memo[x][y]
        dfs(abs(x),abs(y))
        return memo[abs(x)][abs(y)]
