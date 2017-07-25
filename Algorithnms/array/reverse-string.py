# coding=utf-8

'''leetcode 344'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        str = [x for x in s]
        l,r = 0,len(s)-1
        mid = (l+r)//2
        for i in range(0,mid+1):
            str[i],str[r-i] = str[r-i],str[i]
        return ''.join(str)



sol = Solution()
s = "hello."
sol.reverseString(s)