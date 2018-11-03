# -*- coding: utf-8 -*-
# https://leetcode.com/problems/rotate-list/description/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy

        i = 0
        while fast.next:  # Get the total length
            i += 1
            fast = fast.next

        # Get the i-n % i th node
        j = i - k % i
        while j > 0:
            j -= 1
            slow = slow.next

        # Do the rotation
        fast.next, dummy.next, slow.next = dummy.next, slow.next, None

        return dummy.next
