class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        address = set()
        for email in emails:
            local_name, domain_name = email.split("@")[0], email.split("@")[1]
            local_name = local_name.replace(".", "")
            local_name = local_name.split("+")[0]
            whole_name = local_name + "@" + domain_name
            address.add(whole_name)
        return len(address)
