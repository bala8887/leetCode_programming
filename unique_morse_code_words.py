class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        A=set()
        dict={}
        lst=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha=list(string.ascii_lowercase)
        for alp,i in zip(alpha,lst):
            dict[alp]=i
        for i in words:
            str_check=""
            for j in i:
                str_check+=dict[j]
            A.add(str_check)
        return len(A)
