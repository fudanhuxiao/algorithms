class Solution:
    def countDigitOne(self, n: int) -> int:
        num = 1
        ans = 0
        while n >= num:
            ans += n//(num*10)*num + min(max(n%(num*10)-num+1, 0), num)
            num *= 10
        return ans
