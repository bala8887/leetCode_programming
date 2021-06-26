class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1;
        if len(s)==0:
            return 0;
        final_str='';
        prev_str='';
        ind=0;
        lngth=0;
        for i in s:
            if ind==0:
                ind=1;
                final_str=i;
                prev_str=i;
            else:
                if i in final_str:
                    if lngth<len(final_str):
                        lngth=len(final_str);
                    final_str=final_str[final_str.index(i)+1:len(final_str)]+i;
                else:
                    final_str+=i;
                    prev_str=i;
        if lngth==0:
            return len(s);
        return max(lngth,len(final_str));
