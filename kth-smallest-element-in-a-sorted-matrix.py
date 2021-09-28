class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        while start < end:
            mid = (start+end)//2
            count, low, high = self.binarySearch(matrix, mid, matrix[0][0], matrix[n-1][n-1])
            if count == k:
                return low
            elif count > k:
                end = low
            else:
                start = high
        return end
    
    def binarySearch(self, matrix, mid, low, high):
        count, n = 0, len(matrix)
        row, col = n-1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                high = min(high, matrix[row][col])
                row -= 1
            else:
                low = max(low, matrix[row][col])
                count += row+1
                col += 1
        return count, low, high
        
