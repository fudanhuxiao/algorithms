class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0]*10 for _ in range(10)]
        skip[1][3], skip[3][1], skip[1][7], skip[7][1], skip[3][9], skip[9][3], skip[7][9], skip[9][7] = 2, 2, 4, 4, 6, 6, 8, 8
        skip[1][9], skip[9][1], skip[2][8], skip[8][2], skip[3][7], skip[7][3], skip[4][6], skip[6][4] = 5, 5, 5, 5, 5, 5, 5, 5
        
        def helper(prev, remain, visited):
            if remain == 0:
                return 1
            ans = 0
            for num in range(1, 10):
                if num not in visited and skip[prev][num] in visited:
                    visited.add(num)
                    ans += helper(num, remain-1, visited)
                    visited.remove(num)
            return ans
        
        patterns = 0
        for i in range(m, n+1):
            patterns += 4*helper(1, i-1, set([0,1]))
            patterns += 4*helper(2, i-1, set([0,2]))
            patterns += helper(5, i-1, set([0,5]))
        return patterns
            
            
