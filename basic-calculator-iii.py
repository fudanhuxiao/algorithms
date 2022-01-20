class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            n = 0
            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    n = n*10+int(c)
                if c == '(':
                    n = helper(s)
                if not c.isdigit() or len(s) == 0: # including +-*/)(
                    if sign == '+':
                        stack.append(n)
                    elif sign == '-':
                        stack.append(-n)
                    elif sign == '*':
                        stack[-1] = stack[-1]*n
                    elif sign == '/':
                        stack[-1] = int(stack[-1]/float(n))
                    sign = c
                    n = 0
                if c == ')':
                    break
            return sum(stack)
        return helper(deque(s))
                    
