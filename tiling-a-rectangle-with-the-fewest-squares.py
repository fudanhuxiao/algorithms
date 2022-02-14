class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @lru_cache(None)
        def dfs(x, y):
            if x == y:
                return 1
            if x == 1:
                return y
            if y == 1:
                return x
            ans = x*y
            for i in range(1, x//2+1):
                ans = min(ans, dfs(i, y)+dfs(x-i, y))
            for j in range(1, y//2+1):
                ans = min(ans, dfs(x, j)+dfs(x, y-j))
            for size in range(1, min(x, y)):
                for i in range(1, x-size):
                    for j in range(1, y-size):
                        p1 = dfs(i, y-j)
                        p2 = dfs(i+size, j)
                        p3 = dfs(x-i-size, j+size)
                        p4 = dfs(x-i, y-j-size)
                        p5 = 1
                        ans = min(ans, p1+p2+p3+p4+p5)
            return ans
        return dfs(m, n)
