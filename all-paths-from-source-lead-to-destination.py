class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for frm, to in edges:
            graph[frm].append(to)
        def dfs(frm, visited):
            visited.add(frm)
            if frm not in graph:
                return frm == destination
            for to in graph[frm]:
                if to in visited or not dfs(to, visited):
                    return False
                visited.remove(to)
            return True
        return dfs(source, set())
