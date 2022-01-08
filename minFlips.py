class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        def toTuple(status):
            ls = []
            for i in range(len(status)):
                for j in range(len(status[0])):
                    ls.append(status[i][j])
            return tuple(ls)
        new = toTuple(mat)
        queue = deque([new])
        visited = set([new])
        ans, end = 0, tuple([0]*(n*m))
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == end:
                    return ans
                for i in range(m*n):
                    r, c = i//n, i%n
                    copy = list(cur)
                    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0],[0,0]]:
                        nr, nc = r+dr, c+dc
                        if nr >= 0 and nc >= 0 and nr < m and nc < n:
                            j = nr*n+nc
                            copy[j] = 1 - copy[j]
                    newtuple = tuple(copy)
                    if newtuple not in visited:
                        visited.add(newtuple)
                        queue.append(newtuple)
            ans += 1
        return -1
