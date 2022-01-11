class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        maxheap = []
        for cnt, char in [[a, 'a'], [b, 'b'], [c, 'c']]:
            if cnt > 0:
                heappush(maxheap, (-cnt, char))
        while maxheap:
            temp = None
            if len(ans) >= 2 and ans[-1] == ans[-2] and ans[-1] == maxheap[0][1]:
                temp = heappop(maxheap)
            if not maxheap:
                break
            cnt, char = heappop(maxheap)
            ans.append(char)
            if cnt + 1 < 0:
                heappush(maxheap, (cnt+1, char))
            if temp:
                heappush(maxheap, temp)
        return ''.join(ans)
