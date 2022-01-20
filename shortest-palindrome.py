#Rabin Karp
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        base, mode = 26, 10**9+7
        left, right = 0, 0
        mul, best = 1, -1
        for i in range(n):
            left = (left*base + ord(s[i])-ord('a'))%mode
            right = (right + (ord(s[i])-ord('a'))*mul)%mode
            mul *= base
            if left == right:
                best = i
        s1 = '' if best == n-1 else s[best+1:]
        return s1[::-1]+s
