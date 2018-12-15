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
  def deleteDuplicates(self, head):
    """
    :type head ListNode
    """
    if not head:
      return head

    dummy = ListNode(-1)
    dummy.next = head
    head = dummy

    while head.next and head.next.next:

      if head.next.val == head.next.next.val:
        val = head.next.val
        while head.next and head.next.val == val:
          head.next = head.next.next
      else:
        head = head.next
    return dummy.next
