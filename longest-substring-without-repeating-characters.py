# -*- coding: utf-8 -*-
class Solution:

  def lengthOfLongestSubstring1(self, s):
    """Got lenght of the longest sub string of given string.
    
    Arguments:
      s {[str]} -- [the source string]
    
    Returns:
      [int] -- [the length of the longest substring]
    """

    ans = 0
    for i, c in enumerate(s):
      c_set = set()
      c_set.add(c)
      for j in range(i + 1, len(s)):
        if s[j] in c_set:
          break
        else:
          c_set.add(s[j])
      ans = max(ans, len(c_set))

    return ans

  def lengthOfLongestSubstring2(self, s):
    ans, left, right = 0, 0, 0
    c_set = set()
    while right < len(s):
      if s[right] not in c_set:
        c_set.add(s[right])
        right += 1
        ans = max(ans, len(c_set))
      else:
        c_set.remove(s[left])
        left += 1

    return ans