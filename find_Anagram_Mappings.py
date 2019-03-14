class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dict={}
        list=[]
        for counter,i in enumerate(B,0):
            dict[i]=counter
        for i in A:
            list.append(dict[i])
        
        return list
