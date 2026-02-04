import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        union_find = UnionFind(len(accounts))

        email_to_account_index = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_account_index:
                    union_find.union(i, email_to_account_index[email])
                email_to_account_index[email] = i

        account_emails = collections.defaultdict(list)
        for email, account_index in email_to_account_index.items():
            account_emails[union_find.find(account_index)].append(email)

        merged_accounts = []
        for i, emails in account_emails.items():
            merged_accounts.append([accounts[i][0], *sorted(emails)])
        return merged_accounts


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return

        self.parents[parent_x] = parent_y
