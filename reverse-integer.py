class Solution:
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        res = '-' if x < 0 else ''
        x = abs(x)
        while x > 0:
            x, mod = divmod(x, 10)
            res += str(mod)
        rst = int(res)
        return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0
