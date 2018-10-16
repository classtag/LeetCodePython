# -*- coding: utf-8 -*-
# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []

        q = deque(maxlen=k)
        for idx, num in enumerate(nums):
            # 队尾元素 q[-1]
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(idx)
            # 队头元素 q[0]
            if q[0] == idx - k:
                q.popleft()
            if idx >= k - 1:
                result.append(nums[q[0]])

        return result
