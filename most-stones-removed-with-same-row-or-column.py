class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        islands, removed = 0, set()
        
        def dfs(i, j):
            removed.add((i, j))
            for y in rows[i]:
                if (i, y) not in removed:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) not in removed:
                    dfs(x, j)
        
        for i, j in stones:
            if (i, j) not in removed:
                dfs(i, j)
                islands += 1
        return len(stones)-islands
