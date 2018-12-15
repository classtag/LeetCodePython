# -*- coding: utf-8 -*-


class Solution(object):

  def maxSumSubmatrix(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    L, R = 0, k

    ans = 0
    while L < R:
      mid = (L + R) / 2
      if self.guess():
        ans = mid
        L += 1
      else:
        R = mid

    return ans

  @staticmethod
  def guess():
    pass
