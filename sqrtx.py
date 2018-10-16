# -*- coding: utf-8 -*-
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        L, R = (0, x + 1)  # [0, x+1)
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
