class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if k >= n:
            return total
        subSum = 0
        minSub = total
        for i in range(n):
            subSum += cardPoints[i]
            if i >= n-k-1:
                minSub = min(minSub, subSum)
                subSum -= cardPoints[i-(n-k)+1]
        return total-minSub
                
            
