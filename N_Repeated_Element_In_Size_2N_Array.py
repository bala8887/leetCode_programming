class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A)):
            if(A[i]==A[i+1]):
                return A[i]
