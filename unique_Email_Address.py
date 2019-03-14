class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        output_list=set()
        for i in emails:
            local_name,domain_name=i.split('@')
            local_name="".join(local_name.split('+')[0].split('.'))
            output_list.add(local_name+'@'+domain_name)
        return len(output_list)
