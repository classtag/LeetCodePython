class Solution:

  def __init__(self):
    self.arrows = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
      return 0

    self.grid = grid
    self.M, self.N = len(grid), len(grid[0])
    ans = 0
    for i in range(self.M):
      for j in range(self.N):
        if grid[i][j] == '1':
          self.dfs(i, j)
          ans += 1
    return ans

  def dfs(self, x, y):
    self.grid[x][y] = '0'

    # Loop over four directions that move
    for dx, dy in self.arrows:
      nx, ny = x + dx, y + dy
      if 0 <= nx < self.M and 0 <= ny < self.N and self.grid[nx][ny] == '1':
        self.dfs(nx, ny)
