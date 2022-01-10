class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mode = 10**9+7
        counter = {}
        for n in inventory:
            counter[n] = counter.get(n, 0)+1
        maxheap = []
        for n in counter:
            heappush(maxheap, (-n, counter[n]))
        ans = 0
        while maxheap and orders > 0:
            val, cnt = heappop(maxheap)
            val = -val
            nxt_val = 0 if not maxheap else -maxheap[0][0]
            if (val-nxt_val)*cnt <= orders:
                orders -= (val-nxt_val)*cnt
                ans += ((val+nxt_val+1)*(val-nxt_val)//2)*cnt
                if maxheap:
                    nxt_val, nxt_cnt = heappop(maxheap)
                    heappush(maxheap, (nxt_val, nxt_cnt+cnt))
            else:
                num = orders//cnt
                ans += cnt*(val+val-num+1)*num//2 + (val-num)*(orders%cnt)
                orders = 0
        return ans%mode
                
