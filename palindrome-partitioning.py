# -*- coding: utf-8 -*-
import copy


class Solution:

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, path, results):
        if not s:
            results.append(copy.copy(path))
            return
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], results)

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    list = s.partition("aab")
    for part in list:
        print(part)
