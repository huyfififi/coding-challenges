import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        union_find = UnionFind(len(accounts))

        email_to_account_index = {}
        for account_index, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_account_index:
                    union_find.union(account_index, email_to_account_index[email])
                email_to_account_index[email] = account_index

        account_index_to_emails = collections.defaultdict(list)
        for email, account_index in email_to_account_index.items():
            account_index_to_emails[union_find.find(account_index)].append(email)

        merged_accounts = []
        for account_index, emails in account_index_to_emails.items():
            account_name = accounts[account_index][0]
            merged_accounts.append([account_name, *sorted(emails)])
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
