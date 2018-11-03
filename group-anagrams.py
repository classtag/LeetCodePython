# -*- coding: utf-8 -*-
# 49 https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = defaultdict(list)
        for s in strs:
            hash_map[''.join(sorted(s))].append(s)
        return [v for _, v in hash_map.items()]
