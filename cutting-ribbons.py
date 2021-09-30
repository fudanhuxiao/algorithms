class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if k > sum(ribbons):
            return 0
        def count(length):
            cnt = 0
            for ribbon in ribbons:
                cnt += ribbon//length
            return cnt
        
        start, end = 1, sum(ribbons)//k
        while start + 1 < end:
            mid = (start+end)//2
            cnt = count(mid)
            if cnt >= k:
                start = mid
            else:
                end = mid-1
        return end if count(end) >= k else start
