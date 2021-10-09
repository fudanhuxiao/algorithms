from heapq import *
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n, m = len(servers), len(tasks)
        free = []
        for i in range(n):
            heappush(free, [servers[i], i, 0])
        busy = []
        ans = []
        for j in range(m):
            weight, idx, time = heappop(free)
            heappush(busy, [max(time, j)+tasks[j], weight, idx])
            ans.append(idx)
            while busy and busy[0][0] <= j+1 or not free:
                time, weight, idx = heappop(busy)
                heappush(free, [weight, idx, time])
        return ans
            
            
