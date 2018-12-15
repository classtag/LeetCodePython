# -*- coding: utf-8 -*-


class Solution:

  def findRedundantConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """

    parent = list(range(1005)) # set node's parent to itself.

    def find(v): # find the root this node belongs to
      if v != parent[v]:
        parent[v] = find(parent[v]) # path compression.
      return parent[v]

    for u, v in edges:
      if find(u) == find(v): # if the two ends of an edge has same root, return
        return [u, v]
      else: # else connect the small half to the large half.
        parent[find(u)] = find(v)
    return []
