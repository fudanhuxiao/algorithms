class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def longest(i, j, lastval, memo):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= lastval:
                return 0
            if memo[i][j] > -1:
                return memo[i][j]
            for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                memo[i][j] = max(memo[i][j], 1+longest(x, y, matrix[i][j], memo))
            return memo[i][j]
            
        length, memo = 0, [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = max(length, longest(i, j, float('-inf'), memo))
        return length
