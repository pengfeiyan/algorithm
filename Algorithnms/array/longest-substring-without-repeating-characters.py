# coding=utf-8
'''leetcode 3 滑动窗口'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l,r = 0,-1
        res = 0
        while l < len(s):
            if r+1 < len(s):
                r += 1
                if s[r] not in s[l:r]:
                    res = max(res,r-l+1)
                else:
                    while s[r] in s[l:r]:
                        l += 1
                    res = max(res,r-l+1)
            else:
                return res
        return res

sol = Solution()
a = '0123456'
s = 'abccdef'
print(sol.lengthOfLongestSubstring(s))