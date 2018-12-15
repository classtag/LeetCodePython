from collections import OrderedDict


class LRUCache:

  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.d = OrderedDict()
    self.C = capacity

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    if key in self.d:
      val = self.d.get(key)
      self.d.move_to_end(key, False)
      return val
    return -1

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    if key not in self.d and len(self.d) == self.C:
      self.d.popitem()
    self.d[key] = value
    self.d.move_to_end(key, False)

  # Your LRUCache object will be instantiated and called as such:


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
