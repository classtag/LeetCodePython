# -*- coding: utf-8 -*-


class Solution:

    def strStr(self, source, target):
        """
        find the target from source
        Parameters
        ----------
        source a str
        target a str

        Returns
        -------
        if target exist in source, return the first source index, else return -1
        """
        if not source or not target:
            return -1

        s_len, t_len = len(source), len(target)
        i, j = 0, 0
        for i in range(s_len - t_len + 1):
            for j in range(t_len):
                if source[i + j] != target[j]:
                    break
            if j + 1 == t_len:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()

    index = solution.strStr("ancbbbbb", "bbb")
    assert index == 3
