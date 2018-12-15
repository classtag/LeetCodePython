# -*- coding: utf-8 -*-
class Solution:

  def accountsMerge(self, accounts):
    """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
    n = len(accounts)
    account_sets = list(range(n))

    # find root
    def find_root(idx):
      while account_sets[idx] != idx:
        # path compression
        account_sets[idx] = account_sets[account_sets[idx]]
        idx = account_sets[idx]
      return idx

    # union find
    email_account_idx_map = {} # key:val = email:index
    for account_idx, (_, *emails) in enumerate(accounts):
      for email in emails:
        if email in email_account_idx_map:
          root1 = find_root(account_idx)
          root2 = find_root(email_account_idx_map[email])
          account_sets[root2] = root1
        else:
          email_account_idx_map[email] = account_idx

    # merge accounts
    from collections import defaultdict
    # key:val = index: {set of emails}
    account_idx_emails = defaultdict(set)
    for account_idx in range(n):
      account_idx_emails[find_root(account_idx)] |= set(
          accounts[account_idx][1:])

    # convert into required format
    res = []
    for account_idx, emails in account_idx_emails.items():
      res.append([accounts[account_idx][0]] + sorted(emails))

    return res
