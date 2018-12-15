# -*- coding: utf-8 -*-
class Solution(object):

  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    L, R = (0, x + 1) # [0, x+1)
    ans = 0
    while L < R:
      mid = (L + R) / 2
      if self.guess(mid, x):
        ans = mid
        L = mid + 1
      else:
        R = mid
    return ans

  @staticmethod
  def guess(v, x):
    return v * v <= x

  def mySqrt2(self, x):
    # 牛顿迭代法
    if x == 0:
      return 0
    last, res = 0, 1
    while res != last:
      last = res
      res = (res + x / res) / 2
    return res
