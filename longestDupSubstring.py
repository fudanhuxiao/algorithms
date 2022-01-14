class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        a1, a2, mode1, mode2 = random.randint(26,100), random.randint(26, 100), random.randint(10**9+7, 2**31-1), random.randint(10**9+7, 2**31-1)
        arr = [ord(c)-ord('a') for c in s]
        def check(l):
            al1, al2 = pow(a1,l,mode1), pow(a2,l,mode2)
            n1, n2 = 0, 0
            for i in range(l):
                n1 = (n1*a1 + arr[i])%mode1
                n2 = (n2*a2 + arr[i])%mode2
            seen = {(n1, n2)}
            for i in range(1, n-l+1):
                n1 = (n1*a1 - arr[i-1]*al1 + arr[i+l-1])%mode1
                n2 = (n2*a2 - arr[i-1]*al2 + arr[i+l-1])%mode2
                if (n1, n2) in seen:
                    return i
                seen.add((n1, n2))
            return -1
        start, end = 1, n-1
        ans, length = -1, -1
        while start <= end:
            mid = (start+end)//2
            ret = check(mid)
            if ret != -1:
                start = mid+1
                ans, length = ret, mid
            else:
                end = mid-1
        return s[ans:ans+length] if ans != -1 else ''
