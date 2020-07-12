"""
    929. Unique Email Addresses (https://leetcode.com/problems/unique-email-addresses/)
"""


class Solution(object):
    def numUniqueEmails(self, emails):
        email_list = []
        for email in emails:
            local, domain = tuple(email.split("@"))
            local = local.replace(".", "")

            if "+" in local:
                local = local.split("+")[0]

            email_list.append(local + "@" + domain)

        total = len(set(email_list))

        return total


sol = Solution()

print(
    sol.numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
)

