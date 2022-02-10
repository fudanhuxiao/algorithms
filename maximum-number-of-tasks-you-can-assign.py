class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        def check(k):
            top_workers = deque()
            w, p = m-1, pills
            for t in range(k-1, -1, -1):
                if top_workers and tasks[t] <= top_workers[0]:
                    top_workers.popleft()
                elif tasks[t] <= workers[w]:
                    w -= 1
                else:
                    maxstrength = top_workers[0] if top_workers else workers[w]
                    if p == 0 or tasks[t] > maxstrength+strength:
                        return False
                    while w >= 0 and workers[w]+strength >= tasks[t]:
                        top_workers.append(workers[w])
                        w -= 1
                    p -= 1
                    top_workers.pop()
            return True                
                    
        start, end = 0, min(m, n)
        while start + 1 < end:
            mid = (start+end)//2
            if check(mid):
                start = mid
            else:
                end = mid
        return end if check(end) else start
