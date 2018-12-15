# -*- coding: utf-8 -*-
import copy


class Solution:
  mapping = ["", "", "abc", 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
      return []
    result = []
    self.recurse(digits, result, "", 0)
    return result

  def recurse(self, digits, result, path, pos):
    """
    :type digits: str
    :type result: list
    :type path: str
    :type pos: int
    """
    if len(path) == len(digits):
      result.append(copy.copy(path))
      return

    for i in range(pos, len(digits)):
      mid = int(digits[i])
      for step in self.mapping[mid]:
        self.recurse(digits, result, path + step, i + 1)


if __name__ == '__main__':
  s = Solution()
  list = s.letterCombinations("23")
  for element in list:
    print(element)
