def solve_knapsack(profits, weights, capacity):
  # optimal solution for knapsack, where space complexity if O[capacity]
  n = len(profits)
  if n != len(weights) or n <= 0 or capacity <= 0:
    return 0
  dp = [0 for i in range(capacity+1)]
  for c in range(capacity+1):
    if weights[0] <= c:
      dp[c] = profits[0]
  for i in range(1, n):
    for c in range(capacity, 0, -1):
      if weights[i] <= c:
        profit1 = profits[i] + dp[c-weights[i]]
      else:
        profit1 = 0
      profit2 = dp[c]
      dp[c] = max(profit1, profit2)
  return dp[capacity]
