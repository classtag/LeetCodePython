# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)

        if left is None:
            return right
        if right is None:
            return left

        return root

    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if not root or root == p or root == q:
                return root

            if self.is_eq_or_child(p, q):
                return p
            if self.is_eq_or_child(q, p):
                return q

            # dfs left tree, if the p and q are all in left tree, assign root.left to root
            if self.is_eq_or_child(root.left, p) and self.is_eq_or_child(root.left, q):
                root = root.left

            # dfs right tree, if the p and q are all in right tree, assign root.left to root
            if self.is_eq_or_child(root.right, p) and self.is_eq_or_child(root.right, q):
                root = root.right
            else:
                return root

    def is_eq_or_child(self, mother, child):
        """
        Recursion check the child is a child node or equal current mother node.
        :type mother: TreeNode
        :type child: TreeNode
        :rtype:bool
        """
        if mother:
            if mother == child:
                return True
            else:
                return self.is_eq_or_child(mother.left, child) or \
                       self.is_eq_or_child(mother.right, child)
        return False
