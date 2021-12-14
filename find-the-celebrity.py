# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        seen = {}
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
                seen[(celebrity, i)] = True
        for i in range(n):
            if i != celebrity:
                celebrity_i = seen[(celebrity, i)] if (celebrity, i) in seen else knows(celebrity, i)
                i_celebrity = seen[(i, celebrity)] if (i, celebrity) in seen else knows(i, celebrity)
                if celebrity_i or not i_celebrity:
                    return -1
        return celebrity
