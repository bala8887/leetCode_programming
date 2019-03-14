class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter=0
        for i in J:
            counter+=S.count(i)
        return counter
