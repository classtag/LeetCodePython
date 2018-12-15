class Solution:
  def minimumTotal(self, triangle):
    """
    :type triangle list
    """
    rows = len(triangle)
    dp = [[0] * len(triangle[row]) for row in range(rows)]

    for i in range(len(triangle[rows - 1])):
      dp[rows - 1][i] = triangle[rows - 1][i]

    for i in range(rows - 2, -1, -1):
      for j in range(i + 1):
        dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
    return dp[0][0]
