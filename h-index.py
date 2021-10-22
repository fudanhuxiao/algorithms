class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0]*(n+1)
        for c in citations:
            papers[min(c,n)] += 1
        h = n
        paperCnt = 0
        while h >= 0:
            paperCnt += papers[h]
            if paperCnt >= h:
                return h
            h -= 1
