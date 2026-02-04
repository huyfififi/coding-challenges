import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_name = {}
        email_to_neighbors = collections.defaultdict(set)
        for account in accounts:
            name, hub, *rest = account
            email_to_name[hub] = name
            for email in rest:
                email_to_name[email] = name
                email_to_neighbors[email].add(hub)
                email_to_neighbors[hub].add(email)

        visited = set()

        def traverse_email_group(email: str) -> list[str]:
            emails_in_same_group = []
            emails_to_visit = [email]
            while emails_to_visit:
                visiting = emails_to_visit.pop()
                if visiting in visited:
                    continue

                for neighbor in email_to_neighbors[visiting]:
                    emails_to_visit.append(neighbor)
                emails_in_same_group.append(visiting)
                visited.add(visiting)

            return emails_in_same_group

        merged_accounts = []
        for email in email_to_name:
            if email in visited:
                continue

            emails_in_same_group = traverse_email_group(email)
            merged_accounts.append(
                [email_to_name[email], *sorted(emails_in_same_group)]
            )

        return merged_accounts
