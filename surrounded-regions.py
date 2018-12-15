class Solution:

  def __init__(self):
    self.arrows = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if not board:
      return None

    self.board = board
    self.M, self.N = len(board), len(board[0])
    for i in range(self.M):
      for j in range(self.N):
        if i == 0 or j == 0 or i == self.M - 1 or j == self.N - 1:
          if board[i][j] == 'O':
            self.dfs(i, j)

    for i in range(self.M):
      for j in range(self.N):
        if board[i][j] == '#':
          board[i][j] = 'O'
        else:
          board[i][j] = 'X'

  def dfs(self, x, y):
    self.board[x][y] = '#'
    for dx, dy in self.arrows:
      nx, ny = x + dx, y + dy
      if 0 <= nx < self.M and 0 <= ny < self.N and self.board[nx][ny] == 'O':
        self.dfs(nx, ny)
