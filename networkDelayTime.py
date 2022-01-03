class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for frm, to, time in times:
            graph[frm].append([to, time])
        dist = {}
        minheap = [(0, k)]
        while minheap:
            d, node = heappop(minheap)
            if node not in dist:
                dist[node] = d
                for nei, d2 in graph[node]:
                    if nei not in dist:
                        heappush(minheap, (d+d2, nei))
        return max(dist.values()) if len(dist) == n else -1
        
