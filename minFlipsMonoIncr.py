class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, flips = 0, 0
        for c in s:
            ones += int(c)
            flips = min(ones, 1-int(c)+flips)
        return flips
            
