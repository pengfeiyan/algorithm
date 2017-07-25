# coding = utf-8

'''leetcode 125'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = []
        for i in s:
            if i.isnumeric() or i.isalpha():
                string.append(i.upper())
        l,r = 0,len(string)-1
        while l < r:
            if string[l] == string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

sol = Solution()
s = 'aa'
print(sol.isPalindrome(s))