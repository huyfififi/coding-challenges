class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        aggregator = AccountAggregator(accounts)
        for i in range(len(accounts) - 1):
            for j in range(i, len(accounts)):
                if aggregator.email_overlap_exists(i, j):
                    aggregator.union(i, j)
        return aggregator.retrieve_merged_accounts()


class AccountAggregator:
    def __init__(self, accounts: list[list[str]]) -> None:
        self.parents = []
        self.names: list[str] = []
        self.emails: list[set[str]] = []
        for i, account in enumerate(accounts):
            self.parents.append(i)
            self.names.append(account[0])
            self.emails.append(set(account[1:]))

    def find(self, account: int) -> int:
        if self.parents[account] != account:
            self.parents[account] = self.find(self.parents[account])
        return self.parents[account]

    def union(self, account1: int, account2: int) -> None:
        parent1 = self.find(account1)
        parent2 = self.find(account2)

        if parent1 == parent2:
            return

        parent1_size = len(self.emails[parent1])
        parent2_size = len(self.emails[parent2])
        if parent1_size > parent2_size:
            parent1, parent2 = parent2, parent1

        self.parents[parent1] = parent2
        self.emails[parent2] |= self.emails[parent1]

    def email_overlap_exists(self, account1: int, account2: int) -> bool:
        return self.emails[account1] & self.emails[account2]

    def retrieve_merged_accounts(self) -> list[list[str]]:
        checked = set()
        merged_accounts = []
        for account in range(len(self.parents)):
            representative = self.find(account)
            if representative in checked:
                continue

            checked.add(representative)
            account_name = self.names[representative]
            merged_accounts.append([account_name, *sorted(self.emails[representative])])
        return merged_accounts
