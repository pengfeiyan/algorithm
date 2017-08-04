'''leetcode 20 栈'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = set(['(','[','{'])
        right = set([')',']','}'])
        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                if stack:
                    match = stack.pop()
                    if i == ')' and match == '(':
                        continue
                    elif i == ']' and match == '[':
                        continue
                    elif i == '}' and match == '{':
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True

sol = Solution()
s = ''
print(sol.isValid(s))