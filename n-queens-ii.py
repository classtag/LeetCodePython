# -*- coding: utf-8 -*-


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col, pie, na = 0, 0, 0

        self.count = 0

        def dfs(row, col, pie, na):
            if row >= n:
                self.count += 1
                return

            bits = (~(col | pie | na)) & ((1 << n) - 1)
            while bits > 0:
                p = bits & -bits
                dfs(row + 1, col | p)
                bits &= bits - 1
