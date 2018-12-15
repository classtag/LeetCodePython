# -*- coding: utf-8 -*-
# 242 https://leetcode.com/problems/valid-anagram/


class Solution:

  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False
    table = [0] * 26
    start = ord('a')
    for sc, tc in zip(s, t):
      table[ord(sc) - start] += 1
      table[ord(tc) - start] -= 1
    for v in table:
      if v != 0:
        return False
    return True

  def isAnagram0(self, s, t):
    if len(s) != len(t):
      return False
    hash_map = {}
    for sc, tc in zip(s, t):
      hash_map[sc] = hash_map.get(sc, 0) + 1
      hash_map[tc] = hash_map.get(tc, 0) - 1
    for v in hash_map.values():
      if v != 0:
        return False
    return True

  def isAnagram1(self, s, t):
    """
        O(n * log(n))
        :param s:
        :param t:
        :return:
        """
    return sorted(s) == sorted(t)

  def isAnagram2(self, s, t):
    """
        :type s: str
        :type t: str
        :rtype: bool
        """
    if len(s) != len(t):
      return False

    dict_s, dict_t = {}, {}
    for (sc, tc) in zip(s, t):
      dict_s[sc] = dict_s.get(sc, 0) + 1
      dict_t[tc] = dict_t.get(tc, 0) + 1

    return dict_s == dict_t

  def isAnagram3(self, s, t):
    """
        O(n)
        :type s: str
        :type t: str
        :rtype: bool
        """
    if len(s) != len(t):
      return False

    hash_map = dict()
    for c in s:
      hash_map[c] = hash_map.get(c, 0) + 1
    for c in t:
      if c not in hash_map:
        return False
      hash_map[c] = hash_map.get(c) - 1
      if hash_map[c] == 0:
        hash_map.pop(c)

    return len(hash_map) == 0
