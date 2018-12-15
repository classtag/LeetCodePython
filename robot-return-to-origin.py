# -*- coding: utf-8 -*-


class Solution:

  def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    x, y = 0, 0
    for step in moves:
      if step == 'U':
        y += 1
      elif step == 'D':
        y -= 1
      elif step == 'R':
        x += 1
      else:
        x -= 1
    return x == y == 0
