class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph, n = defaultdict(set), len(routes)
        for i in range(n):
            left = set(routes[i])
            for j in range(i+1, n):
                right = set(routes[j])
                if left & right:
                    graph[i].add(j)
                    graph[j].add(i)
        queue, visited, targets = deque(), set(), set()
        for i in range(n):
            for stop in routes[i]:
                if stop == source and i not in visited:
                    visited.add(i)
                    queue.append(i)
                elif stop == target:
                    targets.add(i)
        ans = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur in targets:
                    return ans
                for child in graph[cur]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            ans += 1
        return -1
            
                
