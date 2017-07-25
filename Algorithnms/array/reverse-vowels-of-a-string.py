# coding=utf-8
import time
'''leetcode 345'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = [ x for x in s ]
        l,r = 0,len(str)-1
        '''set查询某值是否在，效率比list快。list转化成set并不需要多少时间，但是转化成set会去重，但是并不影响原list'''
        vow = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while l < r:
            if str[l] not in vow:
                l += 1
            if str[r] not in vow:
                r -= 1
            if str[l] in vow and str[r] in vow:
                str[r],str[l] = str[l],str[r]
                l += 1
                r -= 1
        return ''.join(str)

    def vaildVow(self,e):
        vow = ['a','e','i','o','u','A','E','I','O','U']
        if e in vow:
            return True
        else:
            return False

sol = Solution()
s = "leetcode"
start = time.time()
for i in range(10000):
    sol.reverseVowels(s)
print((time.time()-start))