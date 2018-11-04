# -*- coding: utf-8 -*-
class Solution:
    def myPow0(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 10^10
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow1(x, -n)
        if n % 2 == 1:
            return x * self.myPow1(x, n - 1)
        return self.myPow1(x * x, n // 2)

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n & 1:  # 如果n是奇数
                ans *= x
            x *= x
            n >>= 1  # 相当于整除2
        return ans
