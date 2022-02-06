class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            indegree[a] += 1
            graph[b].append(a)
            indegree[b] += 1
        queue = deque()
        for i in indegree:
            if indegree[i] == 1:
                queue.append(i)
                indegree[i] -= 1
        ans = 0
        remain = len(edges)+1
        while remain > 2:
            size = len(queue)
            for _ in range(size):
                i = queue.popleft()
                for child in graph[i]:
                    indegree[child] -= 1
                    if indegree[child] == 1:
                        queue.append(child)
            remain -= size
            ans += 1
        return ans*2 + (0 if remain == 1 else 1)
