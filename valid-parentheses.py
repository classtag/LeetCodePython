# -*- coding: utf-8 -*-


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or stack.pop() != paren_map[c]:
                return False

        return not stack
