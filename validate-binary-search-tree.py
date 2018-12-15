# -*- coding: utf-8 -*-
# Definition for a binary tree node.


class TreeNode:

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:

  def isValidBST1(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    inorder = self.inorder(root)
    return inorder == list(sorted(set(inorder)))

  def inorder(self, root):
    """
    :type root: TreeNode
    :rtype: list
    """
    if root is None:
      return []
    return self.inorder(root.left) + [root.val] + self.inorder(root.right)

  def isValidBST2(self, root):
    self.prev = None
    return self.helper(root)

  def helper(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
      return True
    if not self.helper(root.left):
      return False
    if self.prev and self.prev.val >= root.val:
      return False
    self.prev = root
    return self.helper(root.right)
