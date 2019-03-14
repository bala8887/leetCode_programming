class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lst=[]
        for i in A:
          lst.append(i*i)
        lst.sort()
        return lst
