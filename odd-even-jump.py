class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        pairs = sorted([(arr[i], i) for i in range(n)], reverse=True)
        odd_jump = self.get_jump(pairs)
        pairs = sorted(pairs, key=lambda x: (x[0], -x[1]))
        even_jump = self.get_jump(pairs)
        # dp = array of n x 2
        # dp[i][0] can we jump to n - 1 when we arrive i by even jumps
        # dp[i][1] can we jump to n - 1 when we arrive i by odd jumps
        
        dp = [[False]*2 for _ in range(n)]
        dp[n - 1][0] = dp[n - 1][1] = True
        
        answer = 1
        for i in range(n - 2, -1, -1):
            dp[i][0] = dp[odd_jump[i]][1] if odd_jump[i] is not None else False
            dp[i][1] = dp[even_jump[i]][0] if even_jump[i] is not None else False
            if dp[i][0] == True:
                answer += 1
        return answer
        
    def get_jump(self, pairs):
        jump, stack = [None] * len(pairs), []
        for value, index in pairs:
            while stack and stack[-1] <= index:
                stack.pop()
            if stack:
                jump[index] = stack[-1]
            stack.append(index)
        return jump
        
        
