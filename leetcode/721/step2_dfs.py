import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_name: dict[str, str] = {}
        email_to_neighbors: dict[str, set[str]] = collections.defaultdict(set)
        for account in accounts:
            name, hub, *rest = account
            email_to_name[hub] = name
            for email in rest:
                email_to_name[email] = name
                email_to_neighbors[hub].add(email)
                email_to_neighbors[email].add(hub)

        visited = set()

        def traverse(email: str) -> list[str]:
            account_emails = []
            emails_to_visit = [email]
            while emails_to_visit:
                visiting = emails_to_visit.pop()
                if visiting in visited:
                    continue

                for neighbor in email_to_neighbors[visiting]:
                    emails_to_visit.append(neighbor)
                account_emails.append(visiting)
                visited.add(visiting)

            return account_emails

        merged_accounts: list[list[str]] = []
        for email in email_to_name:
            if email in visited:
                continue

            account_emails = traverse(email)
            merged_accounts.append([email_to_name[email], *sorted(account_emails)])

        return merged_accounts
