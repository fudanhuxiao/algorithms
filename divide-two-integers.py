class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = -dividend if dividend < 0 else dividend
        divisor = -divisor if divisor < 0 else divisor
        if dividend == 0 or divisor == 1:
            if positive and dividend > 2**31-1:
                return 2**31-1
            if not positive and dividend > 2**31:
                return -2**31
            return dividend if positive else -dividend
        quotient = 0
        while dividend >= divisor:
            temp, cnt = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += cnt
                cnt += cnt
                temp += temp
            if positive and dividend > 2**31-1:
                return 2**31-1
            if not positive and dividend > 2**31:
                return -2**31
        return quotient if positive else -quotient
            
        
