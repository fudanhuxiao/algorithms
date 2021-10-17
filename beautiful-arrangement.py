class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False for i in range(n+1)]
        self.count = 0
        def permute(idx, n):
            if idx > n:
                self.count += 1
            for i in range(1, n+1):
                if not visited[i] and (i % idx == 0 or idx % i == 0):
                    visited[i] = True
                    permute(idx+1, n)
                    visited[i] = False
        permute(1, n)
        return self.count
            
        
