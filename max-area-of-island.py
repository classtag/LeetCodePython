# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.arrows = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        self.grid = grid
        self.M, self.N = len(grid), len(grid[0])
        ans = 0
        for i in range(self.M):
            for j in range(self.N):
                if grid[i][j] == 1:
                    deep = self.dfs(i, j, 0)
                    ans = max(ans, deep)
        return ans

    def dfs(self, x, y, deep):
        self.grid[x][y] = 0
        deep += 1

        # Loop over four directions that move
        for dx, dy in self.arrows:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.M and 0 <= ny < self.N and self.grid[nx][ny] == 1:
                deep += max(self.dfs(nx, ny, deep), deep)

        return deep
