class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort()
        cuboids.sort(key=lambda x:(x[2],x[1],x[0]))
        dp = [0]*n
        for i in range(n):
            premax = 0
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1]:
                    premax = max(premax, dp[j])
            dp[i] = cuboids[i][2] + premax
        return max(dp)
