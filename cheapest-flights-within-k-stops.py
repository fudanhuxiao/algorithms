class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for frm, to, price in flights:
            graph[frm].append([to,price])
        self.dst = dst
        memo = {}
        def dfs(k, frm, memo):
            if frm == self.dst:
                return 0
            if k < 0:
                return float('inf')
            if (frm, k) in memo:
                return memo[(frm, k)]
            curmincost = float('inf')
            for to, curcost in graph[frm]:
                curmincost = min(dfs(k-1, to, memo)+curcost, curmincost)
            memo[(frm, k)] = curmincost
            return curmincost
        mincost = dfs(k, src, memo)
        return mincost if mincost < float('inf') else -1
