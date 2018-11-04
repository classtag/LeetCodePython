# -*- coding: utf-8 -*-
# https://leetcode.com/problems/majority-element/description/

from collections import Counter


class Solution:
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for n in nums:
            d = d.get(n, 0) + 1
        max_count = 0
        max_num = None
        for n, count in d.items():
            if count > max_count:
                max_count = count
                max_num = n
        return max_num

    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major, count = nums[0], 1
        for n in nums[1:]:
            if count == 0:
                count += 1
                major = n
            elif major == n:
                count += 1
            else:
                count -= 1

        return major
