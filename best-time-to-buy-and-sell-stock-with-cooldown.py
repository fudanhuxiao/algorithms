class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, cooled = float('-inf'), float('-inf'), 0
        for p in prices:
            newsold = held+p
            held = max(held, cooled-p)
            cooled = max(cooled, sold)
            sold = newsold
        return max(sold, cooled)
