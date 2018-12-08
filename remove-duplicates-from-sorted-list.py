# -*- coding: utf-8 -*-


"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next=None):
        """
        :type val int
        :type next ListNode
        """
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        """
        :type head ListNode
        """
        if not head or not head.next:
            return head
        dummy = head
        while dummy:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head
