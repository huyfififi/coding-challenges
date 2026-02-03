import collections


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_name = self.construct_email_to_name(accounts)
        email_to_alternatives = self.construct_email_to_alternatives(accounts)

        visited = set()
        merged_accounts = []
        for email in email_to_name:
            if email in visited:
                continue

            emails_in_same_group = self.aggregate_email_in_same_group(
                email=email,
                email_to_alternatives=email_to_alternatives,
                visited=visited,
            )
            merged_accounts.append(
                [email_to_name[email], *sorted(emails_in_same_group)]
            )

        return merged_accounts

    @staticmethod
    def construct_email_to_name(accounts: list[list[str]]) -> dict[str, str]:
        email_to_name = {}
        for name_and_emails in accounts:
            name = name_and_emails[0]
            emails = name_and_emails[1:]
            for email in emails:
                email_to_name[email] = name
        return email_to_name

    @staticmethod
    def construct_email_to_alternatives(
        accounts: list[list[str]],
    ) -> dict[str, set[str]]:
        email_to_alternatives = collections.defaultdict(set)
        for name_and_emails in accounts:
            emails = name_and_emails[1:]
            for email in emails:
                for alternative in emails:
                    if email == alternative:
                        continue
                    email_to_alternatives[email].add(alternative)
        return email_to_alternatives

    @staticmethod
    def aggregate_email_in_same_group(
        email: str, email_to_alternatives: dict[str, set[str]], visited: set[str]
    ) -> list[str]:
        emails_in_same_group = []
        emails_to_check = [email]
        while emails_to_check:
            visiting = emails_to_check.pop()
            if visiting in visited:
                continue

            visited.add(visiting)
            emails_in_same_group.append(visiting)
            for alternative in email_to_alternatives[visiting]:
                emails_to_check.append(alternative)
        return emails_in_same_group
