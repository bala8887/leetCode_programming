class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        max_len=len('{0:b}'.format(x)) if(x>y) else len('{0:b}'.format(y))
        x='{0:b}'.format(x)
        y='{0:b}'.format(y)
        
        x=x.rjust(max_len,'0')
        y=y.rjust(max_len,'0')
        count=0
        for i in range(max_len):
            if(x[i]!=y[i]):
                count+=1
        return count
