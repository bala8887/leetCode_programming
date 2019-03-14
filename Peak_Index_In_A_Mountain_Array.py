class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        centre_element=max(A)
        possible_i=A.index(centre_element)
        if(A[possible_i]>=0 and A[possible_i]<=1000000):
            if(A[possible_i]>A[0] and A[possible_i]>A[len(A)-1]):
                if(len(A)>=3 and len(A)<=10000):
                    return possible_i
        else:
            return 0
